import requests

def get_top_post_of_the_day(subreddit):
    headers = {'User-agent': 'MyBot/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/top/.json?t=day&limit=1'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data['data']['children']:
            top_post = data['data']['children'][0]['data']
            return top_post
        else:
            print(f'No posts found for today in subreddit {subreddit}')
            return None
    else:
        print(f'Error: {response.status_code}')
        return None

def is_external_url(url):
    if 'reddit.com' in url:
        return False
    else:
        return True

def post_to_facebook_group(access_token, group_id, message):
    url = f'https://graph.facebook.com/{group_id}/feed'
    params = {
        'message': message,
        'access_token': access_token
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        print(f'Successfully posted to group {group_id}')
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

subreddit = 'CryptoCurrency'
top_post = get_top_post_of_the_day(subreddit)

if top_post:
    print(f"Title: {top_post['title']}")
    print(f"Score: {top_post['score']}")
    print(f"URL: {top_post['url']}")
    print(f"Is external URL? {is_external_url(top_post['url'])}")

    if is_external_url(top_post['url']):
        access_token = 'EAADEZAC4DDHUBAFPANBzDjq5Rpixtjgm3EIZARpRpLqIhuqdWmMRMf8VSWosrx4OZBOWIMZBtIZAnIvkQR2oOlbZBrWrZAJHzFhQoM1e9QfR3bKZBr0HZBCGrcxpzkQwdgTC4QEZASKgmCDxCR6R4rvBdApMfNpZB9EtP7UFhHn7xWMubkStsdrB1ZCNtnUEfi3Mzwhs2ZCxnNoKvZAx735YsVxUUU'
        group_id = '723683658105357'
        message = top_post['url']

        response = post_to_facebook_group(access_token, group_id, message)
