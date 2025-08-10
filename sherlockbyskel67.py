import requests
from tqdm import tqdm
websites = {
    'Twitter': 'https://twitter.com/{}',
    'instagram.com': 'https://instagram.com/{}',
    'reddit': 'https://www.reddit.com/user/{}',
    'tiktok': 'https://www.tiktok.com/@{}',
    'github': 'https://github.com/{}'
    }

def user(username):
    headers = {'User-Agent': 'Mozilla/5.0'}

    for website, url in tqdm(websites.items(), desc='Checking the websites', unit='website'):
        furl = url.format(username)
        try:
            res = requests.get(furl, headers=headers, timeout=6)
            if res.status_code == 200:
                print(f'user found on | {website} | {furl}')
            else:
                print(f'user not found on {website}')
        except requests.RequestException:
            print(f'error: {website}')

if __name__ == '__main__':
    username = input('Made By skel67\nenter user: ').strip()
    user(username)