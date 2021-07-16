import requests
from bs4 import BeautifulSoup
import os


FILE = 'wikipage.html'
URL = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BF%D1%82%D0%B8%D1%86_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'

def load_url_contents_cached(url, local_file):
    # если есть на диске, то считаем с диска
    if os.path.exists(local_file):
        with open(local_file, 'r', encoding="utf-8") as f:
            contents = f.read()
    else:
        # нет на диске - скачаем
        contents = requests.get(url).text
        
        # сохраним в файл
        with open(local_file, 'w', encoding="utf-8") as f:
            f.write(contents)
    return contents

          

def get_title(contents):
    soup = BeautifulSoup(contents, 'lxml')
    titles = soup.find_all('i')
    lat_titles = []

    for i in range(len(titles)):
        lat_titles.append(titles[i].string)
       
    return lat_titles




def get_wiki_species(species_file):
    content = load_url_contents_cached(URL, FILE)
    lat_species = get_title(content)
    lat_species = lat_species[:893]

    with open('lat_species.txt', 'w', encoding="utf-8") as f:
        for bird in lat_species:
            f.write(bird +'\n')
    
