import requests
import plotly.express as px


#Realiza una llamada a la API y verifica la respuesta.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Procesa los resultados totales.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

#Procesa la información del repositorio.
repo_dicts = response_dict["items"]
repo_links, stars, hover_texts, repo_names = [],[],[], []
for repo_dict in repo_dicts:
    #Convierte los nombres de los repos en enlaces.
    repo_names.append(repo_dict["name"])
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_dict["name"]}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])
    #Construye los textos emergentes.
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

#Crea una visualización.
title = "Los repositorios más populares de Python en GitHub"
labels = {'x': "Repositorio", 'y': "Estrellas"}
fig = px.bar(x=repo_links, y=stars, title = title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20, yaxis_title_font_size = 20)
fig.update_traces(marker_color = 'SteelBlue', marker_opacity = 0.6)
fig.show()