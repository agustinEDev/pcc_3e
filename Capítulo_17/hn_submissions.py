from operator import itemgetter

import requests

#Hace una llamada a la API y verifica la respuesta.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

#Procesa la información sobre cada envío.
submissions_ids = r.json()
submission_dics = []
for submission_id in submissions_ids[:30]:
    #Hace una llamada separada para cada envío.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tStatus Code: {r.status_code}")
    response_dict = r.json()

    #Crea un diccionario para cada artículo.
    submission_dic = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dics.append(submission_dic)

submission_dics = sorted(submission_dics, key=itemgetter('comments'), 
            reverse=True)
for submission_dic in submission_dics:
    print(f"\nTitle: {submission_dic['title']}")
    print(f"Discussion link: {submission_dic['hn_link']}")
    print(f"Comments: {submission_dic['comments']}")