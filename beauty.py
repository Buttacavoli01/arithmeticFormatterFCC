import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup




while True:
    gpath = 'https://google.com/search?q='
    url = input("Search for ")
    google = gpath + url
    html = urllib.request.urlopen(google).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))