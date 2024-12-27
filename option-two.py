import requests # type: ignore

def fetch_data(endpoint):
    """
    Fetches data from the given Hacker News API endpoint.
    
    Args:
        endpoint (str): The API endpoint URL.

    Returns:
        dict | list: Parsed JSON response from the API.
    """
    base_url = "https://hacker-news.firebaseio.com/v0"
    url = f"{base_url}/{endpoint}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {endpoint}: {e}")
        return None

def display_menu():
    """
    Displays a menu of options for the user.
    """
    print("\nSelect an option:")
    print("1. Top Stories")
    print("2. New Stories")
    print("3. Best Stories")
    print("4. Ask HN Stories")
    print("5. Show HN Stories")
    print("6. Job Stories")
    print("7. Get Item Details")
    print("8. Get User Details")
    print("9. Recent Updates")
    print("0. Exit")

def main():
    """
    Main program loop to interact with the Hacker News API.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (0-9): "))
            if choice == 0:
                print("Exiting. Goodbye!")
                break
            elif choice == 1:
                print(fetch_data("topstories"))
            elif choice == 2:
                print(fetch_data("newstories"))
            elif choice == 3:
                print(fetch_data("beststories"))
            elif choice == 4:
                print(fetch_data("askstories"))
            elif choice == 5:
                print(fetch_data("showstories"))
            elif choice == 6:
                print(fetch_data("jobstories"))
            elif choice == 7:
                item_id = input("Enter the item ID: ")
                print(fetch_data(f"item/{item_id}"))
            elif choice == 8:
                username = input("Enter the username: ")
                print(fetch_data(f"user/{username}"))
            elif choice == 9:
                print(fetch_data("updates"))
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the script
if __name__ == "__main__":
    main()
