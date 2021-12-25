import requests
from bs4 import BeautifulSoup
import os
from config import LAT_SPECIES_URL

FILE = 'ebirds.html'
URL = LAT_SPECIES_URL

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
    titles = soup.find_all('em')
    lat_titles = []

    for i in range(len(titles)):
        lat_titles.append(titles[i].string)
       
    return lat_titles




def get_wiki_species():
    content = load_url_contents_cached(URL, FILE)
    species = get_title(content)
    species = species
    print('number of species:', len(species))

    with open('species.txt', 'w', encoding="utf-8") as f:
        for bird in species:
            f.write(bird +'\n')




