
# basics of working with APIs (Application Programming Interface)

import requests

# make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# store the api response in a variable
response_dict = r.json()
print(f"Total Repositories: {response_dict['total_count']}")

# explore information about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returns: {len(repo_dicts)}")

# examine the first repository
print("\n Selected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")