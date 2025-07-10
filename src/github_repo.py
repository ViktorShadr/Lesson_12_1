import requests

def get_github_repos(username: str) -> list[str]:
    list_repo =[]
    repo_url = f"https://api.github.com/users/{username}/repos"
    repo_response = requests.get(repo_url)

    list_repo =  [repo['name'] for repo in repo_response.json()]

    return list_repo

list_users = 'ViktorShadr'
print(get_github_repos(list_users))

