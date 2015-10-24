from bs4 import BeautifulSoup
import requests
import json

def _filter_by_length(tag_content):
    # tag_content --> contenido (en *string*) de la etiqueta.

    min_length = 3
    if tag_content:
        return len(tag_content) > min_length

    return True

def reader(news_url, class_keyword):
    # news_url      --> URL con el cual se obtiene la noticia.
    # class_keyword --> *class-keyword* para ubicar el cuerpo de la noticia.

    r = requests.get(news_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    news_body = soup.find('article', class_=class_keyword)
    content = news_body('p')
    # input()
    # print(content)

def get_news_list(feed_url, html_tag, class_keyword):
    # feed_url      --> URL del *feed*.
    # html_tag      --> etiqueta HTML para ubicar el *feed*.
    # class_keyword --> *class-keyword* para ubicar el *feed*.

    # obtiene el *feed*.
    r = requests.get(feed_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    feed = soup.find(html_tag, class_=class_keyword)

    # luego, filtra según tamaño del contenido.
    filt_feed = feed('a', string=_filter_by_length)
    href_list = [link['href'] for link in filt_feed]

    # por último, elimina posibles duplicados.
    href_list = list(set(href_list))
    return href_list

def load_sources(filename):
    # filename --> nombre del archivo con los *feeds*.

    with open(filename) as src_file:
        sources = json.load(src_file)
        feed_list = []  # lista de *feeds*, o también
                        # lista de listas de noticias.
        for source in sources:
            # print(source.keys())
            news_list = get_news_list(source['feed-url'],
                                 source['feed-tag'],
                                 source['feed-keyword'])

            # con esto, fabrica un diccionario.
            news_dict = {'news-list'    : news_list,
                         'news-keyword' : source['news-keyword']}
            feed_list.append(news_dict)

    return feed_list

def run():
    feed_list = load_sources('sources.json')
    # print(feed_list)
    for feed in feed_list:
        for news_url in feed['news-list']:
            reader(news_url, feed['news-keyword'])
run()
