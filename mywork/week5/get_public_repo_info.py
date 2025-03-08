

import requests
import json

filename = 'repos_atacanbt.json'
file_path = 'mywork/week5/output/' + filename

url = 'https://api.github.com/users/atacanbt/repos'
# url = 'https://api.github.com/repos/atacanbt/WSAA-coursework/contents/assignments'

response = requests.get(url)
print(response.status_code)

repo_json = response.json()
# print(repo_json)

with open(file_path, 'w') as file:
    json.dump(repo_json, file, indent=4)
    print('File created successfully!')
