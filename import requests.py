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
        access_token = 'EAADEZAC4DDHUBAIVtD9MS39ew9KnEVj2rIz1gjIwdpe7fBopVuxRqqmFcjDl120JZABzZA1zPMO2qb4NmZA6Tmoof5aLM7wFYGb1zQHOK5gwfT1aD9clxydfqZCPFotZBXZB9J8o4s6v2MBEn5Pv2nIHykzsioaLyLPwmA7jtjtZClpRACe6W3eCy81S4e3RdZCLLGFPDndPzHNQ6JeAYQSELYEtDaDjzCaZBo9ZBr6AFb7ipDrHt7TCeBB'
        group_id = '723683658105357'
        message = top_post['url']
        response = post_to_facebook_group(access_token, group_id, message)