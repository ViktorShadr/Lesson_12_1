import requests
import os
from dotenv import load_dotenv


def get_github_users(github_users):
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN')
    headers = {"Authorization": f"Bearer {github_token}"}

    url = f"https://api.github.com/users/{github_users}"
    response = requests.get(url, headers=headers)
    user_info = response.json()
    return user_info



users = 'ViktorShadr'
result = get_github_users(users)
print(result)