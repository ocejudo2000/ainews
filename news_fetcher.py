import feedparser
import requests
from bs4 import BeautifulSoup

def fetch_rss_feed(url):
    """Fetches and parses an RSS feed."""
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries:
        articles.append({
            "title": entry.title,
            "link": entry.link,
            "summary": entry.summary
        })
    return articles

def fetch_website(url):
    """Fetches and scrapes a website for links."""
    articles = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # This is a generic scraper and might need to be customized for each site.
        # For now, we'll look for common article link patterns.
        for a in soup.find_all("a", href=True):
            if "/20" in a["href"] and len(a.text) > 50: # A simple filter for article-like links
                articles.append({
                    "title": a.text.strip(),
                    "link": a["href"],
                    "summary": ""
                })
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return articles

def fetch_all_news(sources):
    """Fetches news from all sources."""
    all_articles = []
    for source in sources:
        if source["type"] == "rss":
            all_articles.extend(fetch_rss_feed(source["url"]))
        else:
            all_articles.extend(fetch_website(source["url"]))
    return all_articles
