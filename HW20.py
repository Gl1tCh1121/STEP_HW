import requests
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def fetch_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        return []

def count_posts(all_posts):
    counts = Counter(post['userId'] for post in all_posts)
    return dict(counts)

def find_longest_post(all_posts):
    if not all_posts:
        return None
    longest = max(all_posts, key=lambda post: len(post.get('body', '')))
    return {
        "userId": longest['userId'],
        "title": longest['title'],
        "length": len(longest['body'])
    }

def average_title_length(all_posts):
    if not all_posts:
        return 0.0
    total_length = sum(len(post.get('title', '')) for post in all_posts)
    return round(total_length / len(all_posts), 1)


if __name__ == "__main__":
    user_ids = [1, 2, 3, 4, 5]
    
    print("მონაცემები იტვირთება...")
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_posts, user_ids))
    
    all_posts = [post for user_posts in results for post in user_posts]

    if not all_posts:
        print("მონაცემების წამოღება ვერ მოხერხდა.")
        exit()

    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(count_posts, all_posts)
        f2 = executor.submit(find_longest_post, all_posts)
        f3 = executor.submit(average_title_length, all_posts)

        task1_result = f1.result()
        task2_result = f2.result()
        task3_result = f3.result()

    # 3. შედეგების ბეჭდვა (ნაბიჯი 3)
    print("=" * 40)
    print("        პოსტების ანალიზი")
    print("=" * 40)
    print(f"{'მომხმარებელი':<15} {'პოსტების რაოდენობა'}")
    print("-" * 40)
    for user_id in user_ids:
        count = task1_result.get(user_id, 0)
        print(f"User {user_id:<10} {count}")
    print("-" * 40)
    
    if task2_result:
        print("ყველაზე გრძელი პოსტი:")
        print(f"  მომხმარებელი: User {task2_result['userId']}")
        print(f"  სათაური: \"{task2_result['title'][:40]}...\"")
        print(f"  სიგრძე: {task2_result['length']} სიმბოლო")
    
    print("-" * 40)
    print(f"სათაურების საშუალო სიგრძე: {task3_result} სიმბოლო")
    print("=" * 40)