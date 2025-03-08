import requests
import json
from config import apikeys as cfg

file_name = 'repos_atacanbt_private.json'
file_path = 'mywork/week5/output/' + file_name

url = 'https://api.github.com/repos/atacanbt/a_private_one'

api_key = cfg['github_token']

response = requests.get(url, auth=('token', api_key))
print(response.status_code)

with open(file_path, 'w') as file:
    repo_json = response.json()
    json.dump(repo_json, file, indent=4)
    print('File created successfully!')