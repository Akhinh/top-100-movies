import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire100 = response.text

soup = BeautifulSoup(empire100, "html.parser")
movies = [soup.getText() for soup in soup.find_all("h3", class_="title")[::-1]]

with open("Top_100_movies.txt", encoding="utf8", mode="w") as the_movies:
    for movie in movies:
        the_movies.write(f"{movie}\n")



