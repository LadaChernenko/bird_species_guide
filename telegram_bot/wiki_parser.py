import os
import wikipedia


def get_wiki_info(query):
    wikipedia.set_lang("ru")
    try:
        # bird_name = wikipedia.page(query, results=0)
        # bird_info = wikipedia.summary(bird_name)
        wikipage = wikipedia.page(query)
        title = wikipage.title
        url = wikipage.url
        return title, url
    except wikipedia.exceptions.DisambiguationError as e:
         print(e.options)



