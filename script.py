from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint

def _reader(news_url, title_path, class_keyword):
    # news_url      --> URL con el cual se obtiene la noticia.
    # title_path    --> camino para ubicar el título de la noticia.
    # class_keyword --> *class-keyword* para ubicar el cuerpo de la noticia.

    rget = requests.get(news_url)
    soup = BeautifulSoup(rget.content, 'html.parser')

    # obtiene los valores del *path*.
    t_helptag = title_path[0]
    t_keyword = title_path[1]
    title_tag = title_path[2]

    # obtiene el título.
    helper = soup.find(t_helptag, class_=t_keyword)
    title = helper.find(title_tag).string
    print(title)

    # obtiene el cuerpo de la noticia.
    article = soup.find('div', class_=class_keyword)
    body = [str(paragraph) for paragraph in article('p')]
    # print(body)
    # input()

    return {'title': title, 'body': body}

def _get_news_list(feed_url, html_tag, class_keyword):
    # feed_url      --> URL del *feed*.
    # html_tag      --> etiqueta HTML para ubicar el *feed*.
    # class_keyword --> *class-keyword* para ubicar el *feed*.

    # obtiene el *feed*.
    rget = requests.get(feed_url)
    soup = BeautifulSoup(rget.content, 'html.parser')
    feed = soup.find_all(html_tag, class_=class_keyword)

    # extrae todos los enlaces.
    href_list = [link.find('a')['href'] for link in feed]

    # por último, elimina posibles duplicados.
    # href_list = list(set(href_list))
    pprint(href_list)
    return href_list

def _post_to_api(api_url, contents):
    # api_url  --> URL del API.
    # contents --> diccionario completo de noticias.

    _data = {"contents": json.dumps(contents)}
    rpost = requests.post(api_url, data=_data)
    print(rpost)

def build(filename):
    # filename --> nombre del archivo con los *feeds*.

    # #######################################################
    # Este método busca aprovechar el diccionario subyacente,
    # que se obtiene a partir del archivo JSON.
    # Luego, sólo se debe agregar las noticias,
    # que serían los datos faltantes.
    # ###############################

    feed_list = []  # lista de *feeds*, o también
                    # lista de listas de noticias.
    with open(filename) as src_file:
        all_sources = json.load(src_file)

    for source in all_sources:
        news_list = _get_news_list(source['feed-url'],
                                   source['feed-tag'],
                                   source['feed-keyword'])
        source['news-list'] = []
        for news_url in news_list:
            try:
                # lee la noticia.
                reader = _reader(news_url,
                                 source['title-path'],
                                 source['body-keyword'])

                # fabrica el diccionario con la información.
                news_dict = {'title': reader['title'],
                             'date' : "",
                             'link' : news_url,
                             'body' : reader['body']}
                source['news-list'].append(news_dict)
                # pprint(source)
            except:
                print("Error.")

        # elimina las llaves innecesarias.
        source.pop('feed-url')
        source.pop('feed-tag')
        source.pop('feed-keyword')
        source.pop('body-keyword')
        source.pop('title-path')
        # pprint(source)

    # pprint(all_sources)
    # _post_to_api('http://address', all_sources)

build('sources.json')
