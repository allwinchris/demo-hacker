import firebase_admin  # type: ignore
from firebase_admin import db # type: ignore


def fetch_top_hackernews_articles():
    # Initialize Firebase Admin SDK
    if not firebase_admin._apps:
        firebase_admin.initialize_app(
            options={"databaseURL": "https://hacker-news.firebaseio.com"}
        )

    # Reference to the top stories
    top_stories_ref = db.reference("/v0/topstories")
    top_story_ids = top_stories_ref.get()

    # Fetch details of the top 20 stories
    articles = []
    for story_id in top_story_ids[:20]:
        story_ref = db.reference(f"/v0/item/{story_id}")
        story_data = story_ref.get()
        if story_data:
            articles.append(
                {
                    "title": story_data.get("title"),
                    "url": story_data.get("url"),
                    "score": story_data.get("score"),
                    "author": story_data.get("by"),
                }
            )

    return articles


# Fetch and print the top 20 articles
if __name__ == "__main__":
    top_articles = fetch_top_hackernews_articles()
    for idx, article in enumerate(top_articles, start=1):
        print(
            f"{idx}. {article['title']} ({article['url']}) - Score: {article['score']} by {article['author']}"
        )
