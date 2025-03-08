from github import Github
from config import apikeys as cfg

api_key = cfg['github_token']
g = Github(api_key)

repo = g.get_repo('atacanbt/WSAA-coursework')
print(repo.clone_url)

file_info = repo.get_contents('mywork/week5/test.txt')
url_of_file = file_info.download_url
print(url_of_file)
