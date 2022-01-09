import requests
from bs4 import BeautifulSoup

import re  # regex pattern matcher

import sys  # argument parsing

if len(sys.argv) > 1:
    url = sys.argv[1]

r = requests.get(url)
soup = BeautifulSoup(r.content, features='lxml')

for val in soup.find_all("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")

