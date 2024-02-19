
from bs4 import BeautifulSoup
import requests

URL = 'https://www.kinopoisk.ru/lists/movies/top250'
movie_list = 'https://www.kinopoisk.ru'
response = requests.get(URL)

def get_content():
    response = requests.get(URL) 
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all('div', class_='styles_root__3a8vf')
    movies = []
    for item in items:
        movies.append({
            'title': item.find('span', class_= 'styles_mainTitle__3Bgao').get_text(),
            'mark': item.find('span', class_='styles_kinopoiskValuePositive__1G4F6').get_text(),
            'link': movie_list+item.find('a', class_='base-movie-main-info_link__3BnCh').get('href'),
            'city': item.find('span', class_='desktop-list-main-info_truncatedText__2Q88H').get_text()
        })
    return movies

print(response)
print (get_content())