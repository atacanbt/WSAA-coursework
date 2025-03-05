# get planning applications

import requests
# url = 'https://opendata.arcgis.com/datasets/8f69dffe26324ba3acc653cf6cb5cf8b_0.geojson'
file_path = 'file:///Users/atacanbuyuktalas/Desktop/Data Analytics/WSAA-coursework/mywork/week4/data/Planning_Application_Points.geojson'
response = requests.get(file_path)
list_of_planning = response.json()
print(response.status_code)

print(list_of_planning['features'][0]['geometry']['coordinates'])