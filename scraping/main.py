import feedparser
import requests
import os
import markdownify

# Replace this with the URL of the RSS feed you want to scrape
RSS_FEED_URL = "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"

# Parse the RSS feed
feed = feedparser.parse(RSS_FEED_URL)

# Create a directory to store the MDX files
if not os.path.exists("articles"):
    os.makedirs("articles")

# Loop through all the items in the feed
for item in feed["entries"]:  # Changed from feed["items"] to feed["entries"]
    # Get the title and content of the article
    title = item["title"]
    link = item["link"]
    response = requests.get(link)
    html = response.text

    # Create the content string
    content = f"""date: 2024-06-01T15:32:14Z
tags: ['writings']
draft: false
summary: 'The Time Traveller (for so it will be convenient to speak of him) was
expounding a recondite matter to us. His pale grey eyes shone and
twinkled, and his usually pale face was flushed and animated...'
layout: PostSimple
"""

    # Create the filename for the MDX file
    filename = title.lower().replace(" ", "-") + ".mdx"

    # Write the MDX file
    with open(os.path.join("articles", filename), "w") as f:
        f.write('---\n')  # Removed an extra newline character
        f.write(f"title: {title}\n")
        f.write(content)
        f.write(f"\ncanonicalUrl: {link}")  # Added a newline character before canonicalUrl
        f.write('\n---')
        f.write('\n\n')
        f.write(markdownify.markdownify(html, heading_style="ATX"))  # Removed the split(".") call
