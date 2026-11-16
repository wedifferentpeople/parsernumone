import requests
from bs4 import BeautifulSoup
import csv
import json

data = []
for i in range(1, 11):
    print(f"Парсим страницу №{i}")
    url = f"https://quotes.toscrape.com/page/{i}/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        for q in quotes:
            text = q.find("span", class_="text").text
            author = q.find("small", class_="author").text
            data.append({'text': text, 'author': author})
    except Exception as e:
        print(f"Ошибка на странице {i}: {e}")
        continue
with open("quotes_pro.json", "w", encoding ="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
print(f"Собрано цитат {len(data)}")