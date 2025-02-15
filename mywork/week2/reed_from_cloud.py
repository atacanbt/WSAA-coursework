# read current crypto price from cloud
# author: atacan

import requests
import json

url = 'https://api.coincap.io/v2/assets/bitcoin'
response = requests.get(url)
#print(response.json())

data = response.json()
# with open('data/bitcoin.json', 'w') as file:
#     json.dump(data, file, indent=4)

data = data['data']
# print(data)
rate = data['priceUsd']
print(f'Current Bitcoin price is: {rate} USD')