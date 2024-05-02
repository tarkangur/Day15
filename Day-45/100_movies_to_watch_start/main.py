import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")
print(movies)
movies_title = [i.getText() for i in movies]

with open("movies.txt", "w", encoding="utf-8") as text:
    for i in range(1, 101):
        text.writelines(f"{movies_title[-i]}\n")
