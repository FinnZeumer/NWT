# Information/Documentation of the API under:
# https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS/

import requests

def get_posts():
    url = 'https://api.webapp.prod.blv.foodcase-services.com/BLV_WebApp_WS/webresources/BLV-api/components?lang=en'

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
        print('First Post Title:', posts[0]['name'])
        print('First Post Body:', posts[0]['id'])
    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()