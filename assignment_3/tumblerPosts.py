import json
import re
import requests

# Max number of posts to fetch per API call (Tumblr API pagination)
TUMBLR_API_BATCH_SIZE = 50


def readTumblerJson(blog_name, start, limit):
    """
    Fetch photo posts from a Tumblr blog using v1 API and return as a Python dict.
    Tumblr v1 API returns JavaScript, so this function extracts JSON safely.
    
    Args:
        blog_name (str): Tumblr blog name
        start (int): Pagination start index
        limit (int): Number of posts to fetch in this batch

    Returns:
        dict: Parsed JSON response containing posts and metadata

    Raises:
        ValueError: If the response is invalid or cannot be parsed
    """
    url = f"https://{blog_name}.tumblr.com/api/read/json"
    params = {"type": "photo", "start": start, "num": limit}

    response = requests.get(url, params=params)

    if response.status_code != 200 or not response.text.strip():
        raise ValueError("Invalid Tumblr blog or empty response")

    # Extract JSON object from JavaScript response (v1 API returns JS wrapper)
    match = re.search(r"\{.*\}", response.text, re.DOTALL)
    if not match:
        raise ValueError("Unable to parse Tumblr API response")

    return json.loads(match.group())


def fetchBlogMetadata(blog_name):
    """
    Fetch basic metadata of the blog (title, description, total posts).
    Only fetches 1 post to minimize API calls.
    """
    return readTumblerJson(blog_name, start=0, limit=1)


def fetchAllPosts(blog_name, total_posts):
    """
    Retrieve all photo posts using pagination.
    
    Args:
        blog_name (str): Tumblr blog name
        total_posts (int): Total number of posts to fetch

    Returns:
        list: List of all posts as Python dicts
    """
    posts = []
    start = 0

    # Loop through posts in batches (pagination)
    while start < total_posts:
        response = readTumblerJson(blog_name, start=start, limit=TUMBLR_API_BATCH_SIZE)
        posts.extend(response.get("posts", []))
        start += TUMBLR_API_BATCH_SIZE  

    return posts


def displayBlogInfo(metadata):
    """
    Print blog metadata in a readable format.
    """
    print("\nBlog Information : ")
    print("title:", metadata["tumblelog"]["title"])
    print("name:", metadata["tumblelog"]["name"])
    print("description:", metadata["tumblelog"]["description"])
    print("no of post:", metadata["posts-total"])


def displayImages(posts, start, end):
    """
    Print high-resolution image URLs for posts in the given range.

    Args:
        posts (list): List of post dicts
        start (int): Start index (1-based)
        end (int): End index (1-based)
    """
    print("\nImages:")

    for index in range(start - 1, end):  
        print(f"\n{index + 1}.")
        for photo in posts[index].get("photos", []):
            # Print 1280px resolution photo
            print(photo["photo-url-1280"])


def validateRange(start, end, total_posts):
    return 1 <= start <= end <= total_posts


def main():
   
    blog_name = input("Enter the Tumblr blog name: ").strip()
    start, end = map(int, input("Enter the range (start-end): ").split("-"))

    metadata = fetchBlogMetadata(blog_name)
    total_posts = metadata["posts-total"]

    if not validateRange(start, end, total_posts):
        print("Invalid post range.")
        return

    displayBlogInfo(metadata)

    photo_posts = fetchAllPosts(blog_name, total_posts)
    displayImages(photo_posts, start, end)


if __name__ == "__main__":
    main()
