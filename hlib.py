import requests 
from bs4 import BeautifulSoup

search_item = "cmig4"
base = "http://www.google.com.br"
url = "http://www.google.de/search?q="+ search_item

response = requests.get(url)
soup = BeautifulSoup(response.text,"lxml")
#print (soup.text)

for item in soup.select(".r a"):
    print(item.text)
for next_page in soup.select(".fl"):
    res = requests.get(base + next_page.get('href'))
    soup = BeautifulSoup(res.text,"lxml")
    for item in soup.select(".r a"):
        print(item.text)

#file = open('dump.xml', 'w')
#file.write(soup.text)
#file.close()


#merge lists
def merge(list1, list2): 
    merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return merged_list