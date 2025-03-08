from github import Github
import requests
from config import apikeys as cfg

api_key = cfg['github_token_wsaa']
g = Github(api_key)

repo = g.get_repo('atacanbt/WSAA-coursework')
print(repo.clone_url)

file_info = repo.get_contents('mywork/week5/test.txt')
url_of_file = file_info.download_url
print(url_of_file)

response = requests.get(url_of_file)
content_of_file = response.text
print(content_of_file)

new_contents = content_of_file + '\nThis is a new line added by the script.'
# print(new_contents)

git_hub_response = repo.update_file(file_info.path, 'Updated by script', new_contents, file_info.sha)
print(git_hub_response)
