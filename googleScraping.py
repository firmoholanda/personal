import requests 
from bs4 import BeautifulSoup

def search(search_item):
 
    base = "http://www.google.com.br"
    url = "http://www.google.de/search?q="+ search_item

    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    #print (soup.text)

    for item in soup.select(".r a"):
        print(item.text)
        #return (item.text)
    for next_page in soup.select(".fl"):
        res = requests.get(base + next_page.get('href'))
        soup = BeautifulSoup(res.text,"lxml")
        for item in soup.select(".r a"):
            print(item.text)

search("smartmentor")