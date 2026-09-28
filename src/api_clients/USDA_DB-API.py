# Information/Documentation of the API under:
# https://app.swaggerhub.com/apis/fdcnal/food-data_central_api

api_key = 'auCk1g5aOhjzoEKh0kul2LFA4uaf8pLnbAx7EaYV'

import requests

def get_posts():
    fdcIds = 534358
    url = f'https://api.nal.usda.gov/fdc/v1/foods?fdcIds={fdcIds}&api_key={api_key}'

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
        print('Description of product:', posts[0]['description'])
        # print('First Post Body:', posts[0]['id'])
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()