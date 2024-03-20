import requests
from pathlib import Path
import json
import os
import sys
sys.path.append('../modulos/')
from modulos.file import File

# Make an API call and store the response.
url = 'https://api.tvmaze.com/search/shows?q='
url += input("Enter the tv show name: ")

response = requests.get(url)
print(f"Status code: {response.status_code}")
datos = json.dumps(response.json(), indent=4)
#print(datos)
file = File('tv_shows.json')
datos = []

if response.status_code == 200:
    os.system('clear')
    # Store API response in a variable.
    response_dict = response.json()

    for result in response_dict:
        try:
            print(f"Name: {result['show']['name']}")
            print(f"Rating: {result['show']['rating']['average']}")
            print(f"Year: {result['show']['premiered']}")
            print(f"Genres:")
            for genre in result['show']['genres']:
                print(f"\t{genre}")
            print(f"Official site: {result['show']['officialSite']}")
            print(f"Summary: {result['show']['summary']}\n")
            print(f"Image: {result['show']['image']['original']}\n")
            #Lo guardamos en un diccionario
            dato = {'Name' : result['show']['name'], 
                    'Rating' : result['show']['rating']['average'], 
                    'Year' : result['show']['premiered'], 
                    'Genres' : result['show']['genres'], 
                    'Oficial Site' : result['show']['officialSite'], 
                    'Summary' : result['show']['summary'], 
                    'Image' : result['show']['image']['original']}
            #Escibimos en el fichero el contenido del diccionario
            file.escribir_json(dato)
        except TypeError:
            pass
