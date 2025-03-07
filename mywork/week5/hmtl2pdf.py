# Converts a webpage to a PDF file via API 
# Author: Atacan Buyuktalas

import requests
import urllib.parse
from config import apikeys as cfg

target_url = 'https://google.com'

# API endpoint
api_url = 'https://api.html2pdf.app/v1/generate'
api_key = cfg['html2pdf']

params = {
    'html': target_url,
    'apiKey': api_key
}

parsed_params = urllib.parse.urlencode(params)

request_url = api_url + '?' + parsed_params
print(request_url)

response = requests.get(request_url)

print(response.status_code)
print(response.text)
result = response.content

file_path = 'output.pdf'

with open(file_path, 'wb') as handler:
    handler.write(result)