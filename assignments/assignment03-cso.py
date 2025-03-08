# The program reads Exchequer Account (Historical Series) data from data.cso.ie and store it into cso.json file
# 
# Author: Atacan Buyuktalas

import requests
import json

url = 'https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en'

file_name = 'cso.json'
file_path = 'assignments/' + file_name

def get_cso_data(url):
    response = requests.get(url)
    data = response.json() 

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("Dataset successfully saved to cso.json")

get_cso_data(url)