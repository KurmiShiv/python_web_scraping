import requests
from bs4 import BeautifulSoup
import pandas as pd

title=[]
body=[]
for i in range(1,16):
    topics_url='https://freewebnovel.com/invincible-novel/chapter-'+str(i)+'.html'
    # print(url)
    response = requests.get(topics_url)
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topics_url))
    doc = BeautifulSoup(response.text, 'html.parser')
    
    temp_title= doc.select('div.top > span') # for title 
    for chapter in temp_title:
        title.append(chapter.text)
# print(title)
    temp_para="" #for paragraph
    div_elements = doc.select('div.txt > p')
    # count=len(div_elements)
    for k in div_elements:
        temp_para=temp_para+k.text+"\n"
    body.append(temp_para)
    # for j in range(1,count+1):
    #     temp_body=
    
df=pd.DataFrame({"chapter":title,"para":body})
print(df)
df.to_csv('topics_intern.csv',index=None)
