# Information/Documentation of the API under:
# https://openfoodfacts.github.io/openfoodfacts-server/api/ref-v3/

api_key = 'auCk1g5aOhjzoEKh0kul2LFA4uaf8pLnbAx7EaYV'

import requests

def get_posts():
    fdcIds = 3274080005003
    url = f'https://world.openfoodfacts.net/api/v3.6/product/{fdcIds}.json'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

def main():
    posts = get_posts()

    if posts:
        print(posts[0]['name'])


        # print('Description of product:', posts[0]['description'])
        # print('First Post Body:', posts[0]['id'])
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()