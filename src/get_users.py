import requests

def get_github_users(github_users):
    headers = {"Authorization": "Bearer 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"}

    url = f"https://api.github.com/users/{github_users}"
    response = requests.get(url, headers=headers)
    user_info = response.json()
    return user_info



users = 'ViktorShadr'
result = get_github_users(users)
print(result)