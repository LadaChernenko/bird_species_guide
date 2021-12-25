
# Utils for dataset creation:
 File | What does it do   | Libraries  
--- | --- | ---
[parsing_google_img.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/collecting_dataset/parsing_google_img.py) | download Google Images |   selenium; urllib; user_agent; logging
[russian_bird_list.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/collecting_dataset/russian_bird_list.py) | download species from [Виды птиц Европейской части России](https://www.ebirds.ru/russia/index.html) to txt file  | requests; BeautifulSoup
[utils.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/collecting_dataset/utils.py) | Rename images according to class in each directory; Search more data for minority classes | wikipedia

Before use change [config.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/collecting_dataset/config.py)
