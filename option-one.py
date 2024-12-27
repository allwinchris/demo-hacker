import requests  # type: ignore


def fetch_top_hackernews_articles():
    # Base URL for Hacker News API
    base_url = "https://hacker-news.firebaseio.com/v0"

    # Fetch the top stories IDs
    # trunk-ignore(bandit/B113)
    response = requests.get(f"{base_url}/topstories.json")
    if response.status_code != 200:
        print("Failed to fetch top stories.")
        return []

    top_stories_ids = response.json()

    # Fetch details of the top 20 stories
    articles = []
    for story_id in top_stories_ids[:20]:
        # trunk-ignore(bandit/B113)
        story_response = requests.get(f"{base_url}/item/{story_id}.json")
        if story_response.status_code == 200:
            story_data = story_response.json()
            articles.append(
                {
                    "title": story_data.get("title"),
                    "url": story_data.get("url"),
                    "score": story_data.get("score"),
                    "author": story_data.get("by"),
                }
            )

    for idx, article in enumerate(articles, start=1):
        print(
            f"{idx}. {article['title']} ({article['url']}) - Score: {article['score']} by {article['author']}"
        )


def fetch_new_hackernews_articles():
    # Base URL for Hacker News API
    base_url = "https://hacker-news.firebaseio.com/v0"

    # Fetch the top stories IDs
    # trunk-ignore(bandit/B113)
    response = requests.get(f"{base_url}/newstories.json")
    if response.status_code != 200:
        print("Failed to fetch top stories.")
        return []

    top_stories_ids = response.json()

    # Fetch details of the top 20 stories
    articles = []
    for story_id in top_stories_ids[:20]:
        # trunk-ignore(bandit/B113)
        story_response = requests.get(f"{base_url}/item/{story_id}.json")
        if story_response.status_code == 200:
            story_data = story_response.json()
            articles.append(
                {
                    "title": story_data.get("title"),
                    "url": story_data.get("url"),
                    "score": story_data.get("score"),
                    "author": story_data.get("by"),
                }
            )

    for idx, article in enumerate(articles, start=1):
        print(
            f"{idx}. {article['title']} ({article['url']}) - Score: {article['score']} by {article['author']}"
        )


def fetch_type_hackernews_articles():
    # Base URL for Hacker News API
    base_url = "https://hacker-news.firebaseio.com/v0"

    # Fetch the top stories IDs
    # trunk-ignore(bandit/B113)
    response = requests.get(f"{base_url}/newstories.json")
    if response.status_code != 200:
        print("Failed to fetch top stories.")
        return []

    top_stories_ids = response.json()

    # Fetch details of the top 5 stories

    for story_id in top_stories_ids[:5]:
        # try:

        # trunk-ignore(bandit/B113)
        story_response = requests.get(f"{base_url}/item/{story_id}.json")

        item_data = story_response.json()

        item_type = item_data.get("type")
        if item_type == "story":
            print(f"Item ID {story_id} is a {item_type}")
        else:
            print(f"Item ID {story_id} is a {item_type}")

    # except requests.exceptions.RequestException as e:
    #    print(f"Error fetching item data for ID {story_id}: {e}")
    # except Exception as e:
    #    print(f"An unexpected error occurred for ID {story_id}: {e}")


# Default case function
def default_case():
    print("Invalid option selected.")
    return None


# Dictionary as a case statement with numbers as keys
case_statements = {
    1: fetch_top_hackernews_articles,
    2: fetch_new_hackernews_articles,
    3: fetch_type_hackernews_articles,
}

# Example usage
print("Select an option:")
print("1. fetch_top_hackernews_articles")
print("2. fetch_new_hackernews_articles")
print("3. fetch_type_hackernews_articles")
print("4. Best Stories")
print("5. Ask HN Stories")

try:
    option = int(input("Enter your choice (1-5): "))
    result = case_statements.get(option, default_case)()  # Call the function
    print(result)
except ValueError:
    print("Invalid input! Please enter a number.")
