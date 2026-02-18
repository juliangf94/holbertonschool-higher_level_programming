import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Print the status code
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        #   Parse data into a JSON object (list of dictionaries)
        posts = response.json()

        for post in posts:
            #   We use get because it´s safer than post["title"]
            print(post.get('title'))


def fetch_and_save_posts():
    """
     Fetches all posts and saves id, title, and body into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        # Structure the data: pick only the required fields
        # Using a list comprehension for efficiency
        structured_data = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        # Define CSV column headers
        headers = ['id', 'title', 'body']
        #  Write to posts.csv
        try:
            # newline is used to avoid jumps in line
            with open('posts.csv', 'w', newline="", encoding='utf-8') as csvfile:
                # We give the headers to DictWrite and it orders the data
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                # It writes the first line with headers's names
                writer.writeheader()
                # It takes the list and writes it in the file
                writer.writerows(structured_data)
        # Handle error for in/out operation
        except IOError as e:
            print(f"Error saving CSV: {e}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
