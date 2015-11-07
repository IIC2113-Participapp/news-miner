from bs4 import BeautifulSoup
import requests
import pprint
import json

def _filter_by_length(tag_content):
    # tag_content --> contenido (en *string*) de la etiqueta.

    min_length = 3
    if tag_content:
        return len(tag_content) > min_length

    return True

def _reader(news_url, class_keyword):
    # news_url      --> URL con el cual se obtiene la noticia.
    # class_keyword --> *class-keyword* para ubicar el cuerpo de la noticia.

    rget = requests.get(news_url)
    soup = BeautifulSoup(rget.content, 'html.parser')
    article = soup.find('article', class_=class_keyword)
    body = [str(paragraph) for paragraph in article('p')]
    return body

def _get_news_list(feed_url, html_tag, class_keyword):
    # feed_url      --> URL del *feed*.
    # html_tag      --> etiqueta HTML para ubicar el *feed*.
    # class_keyword --> *class-keyword* para ubicar el *feed*.

    # obtiene el *feed*.
    rget = requests.get(feed_url)
    soup = BeautifulSoup(rget.content, 'html.parser')
    feed = soup.find(html_tag, class_=class_keyword)

    # luego, filtra según tamaño del contenido.
    filt_feed = feed('a', string=_filter_by_length)
    href_list = [link['href'] for link in filt_feed]

    # por último, elimina posibles duplicados.
    href_list = list(set(href_list))
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
                news_dict = {'title': "Título no disponible",
                             'date' : "",
                             'link' : news_url,
                             'body' : _reader(news_url,
                                              source['news-keyword'])}
                source['news-list'].append(news_dict)
                # pprint.pprint(source)
            except:
                print("Error.")

        # elimina las llaves innecesarias.
        source.pop('feed-url')
        source.pop('feed-tag')
        source.pop('feed-keyword')
        source.pop('news-keyword')
        # pprint.pprint(source)

    pprint.pprint(all_sources)
    _post_to_api('http://address', all_sources)

build('sources.json')
