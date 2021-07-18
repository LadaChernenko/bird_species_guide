## Utils for dataset creation:
 File | What does it do   | Libraries  
--- | --- | ---
[parsing_google_img.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/bird_img_parsing/parsing_google_img.py) | download Google Images |   selenium; urllib; user_agent; logging
[parsing_wiki.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/bird_img_parsing/parsing_wiki.py) | download to txt file [wiki. Список птиц России](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BF%D1%82%D0%B8%D1%86_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8) | requests; BeautifulSoup
[bounding_box_generator.py](https://github.com/LadaChernenko/bird_species_guide/blob/main/utils/bounding_box_generator.py) | generate txt file with bounding box coordinate from json | os; pd; json

List of birds species obtained from wikipedia. 
Images for each species were downloaded from google. 


~Alas only first 46 images have been downloaded.~

