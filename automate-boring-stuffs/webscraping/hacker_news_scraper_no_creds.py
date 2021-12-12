import string

import requests
from bs4 import BeautifulSoup

content = ' '


def extract_news(url: string):
    print("Extracting news form HackerNews Website")
    cnt = ' '
    cnt += ('<b> Top Stories: </b>\n' + '<br>' + '-' * 50 + '</br>')
    response = requests.get(url)
    myContent = response.content
    soup = BeautifulSoup(myContent, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + '::' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += '<br>-------<br>'
print(content)
