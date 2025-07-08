from xml.etree.ElementTree import indent

import requests
import os
from dotenv import load_dotenv


def get_github_users(github_users):
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN')
    headers = {"Authorization": f"Bearer {github_token}"}

    url_user = f"https://api.github.com/users/{github_users}"
    url_repos = f"https://api.github.com/users/{github_users}/repos"
    response_user = requests.get(url_user, headers=headers)
    response_repos = requests.get(url_repos, headers=headers)
    user_info = response_user.json()
    user_repos_info = response_repos.json()
    keys_to_select = ['login', 'public_repos', 'name']
    list_info = {}
    for key in keys_to_select:
        if key in user_info:
            list_info[key] = user_info[key]

    names = [user['name'] for user in user_repos_info.values()]

    return list_info, names



users = 'ViktorShadr'
result = get_github_users(users)
print(result)