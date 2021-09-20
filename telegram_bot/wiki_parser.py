import os
import wikipedia


def get_wiki_info(query):
    wikipedia.set_lang("ru")
    try:
        bird_name = wikipedia.search('bird '+query, results=1)
        bird_info = wikipedia.summary(bird_name)
        wikipage = wikipedia.page(bird_name)
        title = wikipage.title
        url = wikipage.url
        return title, bird_info, url
    except wikipedia.exceptions.DisambiguationError as e:
         print(e.options)



