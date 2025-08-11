def generate_executive_summary(articles):
    """Generates a simple executive summary from a list of articles."""
    summary = ""
    for article in articles[:5]:  # Summarize the first 5 articles
        summary += f"- {article['title']}\n"
    return summary

def generate_linkedin_article(articles):
    """Generates a LinkedIn article from a list of articles."""
    if not articles:
        return "", ""

    # For simplicity, we'll use the first article for the LinkedIn post
    main_article = articles[0]
    title = f"Hot Take on the Latest in AI: {main_article['title']}"
    body = f"## {main_article['title']}\n\n{main_article['summary']}\n\nRead more here: {main_article['link']} #AI #ArtificialIntelligence #TechNews"
    
    # For the image, we'll return a placeholder for now
    image_url = f"https://via.placeholder.com/800x400.png?text={main_article['title'].replace(' ', '+')}"

    return title, body, image_url
