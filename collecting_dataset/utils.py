import os
import wikipedia
from parsing_google_img import get_image_links, img_downloading
from config import DATASET_PATH

dataset_path = DATASET_PATH + '/dataset'

list_species = os.listdir(dataset_path)


def rename_imgs(dataset_path):
    '''
    Rename images according to class 
    in each directory

    '''
    list_species = os.listdir(dataset_path)
    for i, species in enumerate(list_species):
        try:
            species_path = dataset_path + '/'+species
            files = os.listdir(species_path)
            for idx, file in enumerate(files):
                os.rename(os.path.join(species_path, file), os.path.join(species_path, ''.join([str(i), '_', str(idx), '.jpg'])))
            print(species, 'files are rename')
        except NotADirectoryError:
            print('not a directory')



def get_minority_classes(dataset_path, threshold):
    '''
    Get list of classes with less data than the threshold
    INPUT:
        dataset_path
        threshold - minimum number of samples 
    OUTPUT:
        less_data_species
    '''
    list_species = os.listdir(dataset_path)
    less_data_species = []
    for species in list_species:
        try:
            sp_path = dataset_path + '/' + species
            count = len([name for name in os.listdir(sp_path) if os.path.isfile(os.path.join(sp_path, name))])
            print(species + ': '+ str(count))
            if count < threshold:
                less_data_species.append(species)
        except NotADirectoryError:
            print('not a directory')
    return less_data_species


# запишем названия для вида на английском и русском в словарь


def get_title(species, language):
    '''
    Get species names in other languages 
    INPUT:
        species - latin name
        language ['en', 'ru'] or another 

    OUTPUT:
        title
    '''
    wikipedia.set_lang(language)
    try:
        bird_name = wikipedia.search(species, results=1)
        wikipage = wikipedia.page(bird_name)
        title = wikipage.title
        return(title)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    except wikipedia.exceptions.WikipediaException:
        print('WikipediaException')


def get_more_data(dataset_dir):
    less_data_species = get_minority_classes(dataset_path, 100)
    bird_names = {}
    for species in less_data_species:
        species = ' '.join(species.split('_'))
        names = []
        eng_name = get_title(species, 'en')
        names.append(eng_name)
        ru_name = get_title(species, 'ru')
        names.append(ru_name)
        print(species, ': ', eng_name, ru_name)    
        bird_names[species] = names

    link_file_path = dataset_dir + 'links/'
    download_dir = dataset_dir + 'dataset/'

    for bird in bird_names.keys():
        print(bird)
        eng_bird = bird_names[bird][0]
        if eng_bird:
            eng_link_file = get_image_links(eng_bird, link_file_path, num_requested = 401)
            img_downloading(bird, eng_link_file, download_dir, 'eng')
        ru_bird = bird_names[bird][1]
        if ru_bird != 'Список птиц России':
            ru_link_file = get_image_links(ru_bird, link_file_path, num_requested = 401)
            img_downloading(bird, ru_link_file, download_dir, 'ru')



if __name__ == "__main__":

    dataset_dir = DATASET_PATH
    get_more_data(dataset_dir)






