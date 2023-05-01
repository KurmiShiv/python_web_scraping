import requests
from bs4 import BeautifulSoup
import pandas as pd

# def get_topics_page():
#     # TODO - add comments
#     topics_url = 'https://github.com/topics'
#     response = requests.get(topics_url)
#     if response.status_code != 200:
#         raise Exception('Failed to load page {}'.format(topics_url))
#     doc = BeautifulSoup(response.text, 'html.parser')
#     return doc

# doc = get_topics_page()

def get_topic_titles(doc):
    selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
    topic_title_tags = doc.find_all('p', {'class': selection_class})
    topic_titles = []
    for tag in topic_title_tags:
        topic_titles.append(tag.text)
    return topic_titles

# titles = get_topic_titles(doc)

# print(len(titles))# 30

# print(titles[:5])# ajax , c++

def get_topic_descs(doc):
    desc_selector = 'f5 color-fg-muted mb-0 mt-1'
    topic_desc_tags = doc.find_all('p', {'class': desc_selector})
    topic_descs = []
    for tag in topic_desc_tags:
        topic_descs.append(tag.text.strip())
    return topic_descs
# topic_descs=get_topic_descs(doc)
# print(topic_descs[:5])


def get_topic_urls(doc):
    topic_link_tags = doc.find_all('a', {'class': 'no-underline flex-1 d-flex flex-column'})
    topic_urls = []
    base_url = 'https://github.com'
    for tag in topic_link_tags:
        topic_urls.append(base_url + tag['href'])
    return topic_urls
# topic_urls=get_topic_urls(doc)
# print(topic_urls[:5])

def scrape_topics():
    topics_url = 'https://github.com/topics'
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    topics_dict = {
        'title': get_topic_titles(doc),
        'description': get_topic_descs(doc),
        'url': get_topic_urls(doc)
    }
    return pd.DataFrame(topics_dict)

topic_df=scrape_topics()
print(topic_df)
topic_df.to_csv('topics.csv',index=None)
