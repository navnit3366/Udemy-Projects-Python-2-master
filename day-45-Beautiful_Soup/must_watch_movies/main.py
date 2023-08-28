import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
movies = soup.find_all(name="h3", class_="title")
print(movies)
