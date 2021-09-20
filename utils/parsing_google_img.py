from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse, quote
import urllib.request
import urllib.error
from user_agent import generate_user_agent
import logging
import time
import random
import os 


bird_classes = ['black kite',
 'chaffinch',
 'common magpie',
 'common raven',
 'crested tit',
 'eurasian jay',
 'eurasian pygmy-owl',
 'eurasian tree sparrow',
 'european turtle-dove',
 'great spotted woodpecker',
 'hazel grouse',
 'northern harrier',
 'rock pigeon',
 'ruddy shelduck',
 'snow goose',
 'snowy owl',
 'waxwing',
 'white stork',
 'white wagtail',
 'willow grouse']
 



def make_dataset_dir(link_path):

    link_file_path = link_path + 'links/'
    download_dir = link_path + 'dataset/'
    if not os.path.exists(link_file_path):
        os.makedirs(link_file_path)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    return link_file_path, download_dir


def get_image_links(query, link_file_path, num_requested = 100):

    query = query
    google_query='+'.join(query.split())
    page="https://www.google.co.in/search?q="+'"'+google_query+'"'+"&source=lnms&tbm=isch"
    # сюда вписать путь до chromedriver`а у себя на компьютере
    DRIVER_PATH = 'C:/Users/hd/Documents/chromdriver/chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
    driver.get(page)
    img_urls = set()
    
    # scroll google images gallery
    number_of_scrolls = int(num_requested / 400) + 1 
    for _ in range(number_of_scrolls):
            for __ in range(10):
                # multiple scrolls needed to show all 400 images
                driver.execute_script("window.scrollBy(0, 1000000)")
                time.sleep(2)
            # to load next 400 images
            time.sleep(1)
            try:
                
                driver.find_element_by_class_name("mye4qd").click()
            except Exception as e:
                print("Process-{0} reach the end of page or get the maximum number of requested images".format(query))
                break

    # find all img url 
    
    # thumbs = driver.find_elements_by_xpath('//a[@class="wXeWr islib nfEiy mM5pbd"]')
    thumbs = driver.find_elements_by_css_selector("img.Q4LuWd")
    

    print(len(thumbs))
    for thumb in thumbs:
            try:
                thumb.click()
                time.sleep(random.randint(1, 6))
            except Exception as e:
                print("Error clicking one thumbnail")  

            url_elements = driver.find_elements_by_xpath('//img[@class="n3VNCb"]')
            for url_element in url_elements:
                try:
                    url = url_element.get_attribute('src')
                except e:
                    print("Error getting one url")
                if url.startswith('http') and not url.startswith('https://encrypted-tbn0.gstatic.com') and not url.startswith('https://media-cdn.tripadvisor.com'):
                    img_urls.add(url)
                    print("Found image url: " + url)
                    
    driver.quit()
    link_path = link_file_path + '_'.join(query.split())+'_links.txt'
    with open(link_path, 'w') as wf:
            for url in img_urls:
                wf.write(url +'\n')
    print('Store all the links in file {0}'.format(link_path))

    len(img_urls)
    return link_path


def img_downloading(query, link_file, download_dir):

    count = 0
    headers = {}

    img_dir = download_dir + '_'.join(query.split()) + '/'
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    # start to download images
    with open(link_file, 'r') as rf:
            for link in rf:
                try:
                    o = urlparse(link)
                    ref = o.scheme + '://' + o.hostname
                    ua = generate_user_agent()
                    headers['User-Agent'] = ua
                    headers['referer'] = ref
                    print('\n{0}\n{1}\n{2}'.format(link.strip(), ref, ua))
                    req = urllib.request.Request(link.strip(), headers = headers)
                    response = urllib.request.urlopen(req)
                    data = response.read()
                    file_path = img_dir + '{0}.jpg'.format(count)
                    with open(file_path,'wb') as wf:
                        wf.write(data)

                    count += 1
                    if count % 10 == 0:
                        print('Process-{0} is sleeping'.format(query))
                        time.sleep(random.randint(4, 10))

                except urllib.error.URLError as e:
                    print('URLError')
                    logging.error('URLError while downloading image {0}reason:{1}'.format(link, e.reason))
                    continue
                except urllib.error.HTTPError as e:
                    print('HTTPError')
                    logging.error('HTTPError while downloading image {0}http code {1}, reason:{2}'.format(link, e.code, e.reason))
                    continue
                except Exception as e:
                    print('Unexpected Error')
                    logging.error('Unexpeted error while downloading image {0}error type:{1}, args:{2}'.format(link, type(e), e.args))
                    continue


# for bird in bird_classes:
#     link_file = get_image_links(bird, link_file_path, num_requested = 100)
#     img_downloading(bird, link_file, download_dir)

if __name__ == "__main__":
    
    dataset_dir = 'c:/Users/hd/Documents/Python projects/bird_species/bird_dataset/'
    # Russian bird specias dataset for classification
    species = []
    with open('lat_species.txt', 'r') as f:
        for bird in f:
            species.append(bird)

    # print(len(species))
    link_file_path, download_dir = make_dataset_dir(dataset_dir)
    
    have_bird = [' '.join(x.split('_')) for x in os.listdir(download_dir)]
    
    for bird in species[1:]:
        if bird[:-1] not in have_bird:
            
            link_file = get_image_links(bird, link_file_path, num_requested = 401)
            img_downloading(bird, link_file, download_dir)

