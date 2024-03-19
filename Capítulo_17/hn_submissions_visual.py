import requests
import plotly.express as px

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
url += "?q=sort:descendants"

r = requests.get(url)
print(f"Status code: {r.status_code}")
response_dict = r.json()

# Procesa la información de las submisiones.
submission_ids = response_dict

submission_dicts = []
for submission_id in submission_ids:
    # Crea una llamada a la API separada para cada submision.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tStatus code: {r.status_code}")
    response_dict = r.json()
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0)
    }
    submission_dicts.append(submission_dict)
#Ordenamos los 500 diccionarios para que los temas más comentados estén en la parte superior.
submission_dicts = sorted(
    submission_dicts, key=lambda x: x["comments"], reverse=True)

submission_links, comments = [], []
#Filtramos por los 30 temas más comentados.
for submission_dict in submission_dicts[:30]:
    title = submission_dict["title"]
    hn_link = submission_dict["hn_link"]
    submission_link = f"<a href='{hn_link}'>{title}</a>"
    submission_links.append(submission_link)
    comments.append(submission_dict["comments"])

# Crea una visualización.
title = "Los temas más populares en Hacker News"
labels = {"x": "Tema", "y": "Comentarios"}
fig = px.bar(x=submission_links, y=comments, title=title, labels=labels)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color="MediumPurple", marker_opacity=0.6)

fig.show()