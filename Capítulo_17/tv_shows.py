import requests
from pathlib import Path
import json
import os

# Make an API call and store the response.
url = 'https://api.tvmaze.com/search/shows?q='
url += input("Enter the tv show name: ")

response = requests.get(url)
print(f"Status code: {response.status_code}")
datos = json.dumps(response.json(), indent=4)
#print(datos)
if response.status_code == 200:
    os.system('clear')
    # Store API response in a variable.
    response_dict = response.json()

    for result in response_dict:
        print(f"Name: {result['show']['name']}")
        print(f"Rating: {result['show']['rating']['average']}")
        print(f"Year: {result['show']['premiered']}")
        print(f"Genres:")
        for genre in result['show']['genres']:
            print(f"\t{genre}")
        print(f"Official site: {result['show']['officialSite']}")
        print(f"Summary: {result['show']['summary']}\n")
        print(f"Image: {result['show']['image']['original']}\n")
