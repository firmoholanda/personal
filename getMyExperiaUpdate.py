import requests 
from bs4 import BeautifulSoup
import xlwt
import smtplib

#site xperia global
url = "https://support.sonymobile.com/global-en/xperiaxa/kb/801930740188bd387015e0fa244400032cc/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

data = []
for item in soup.select("table"):
    #print(table)
    table_body = soup.find('tbody')
    #print(table_body)
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values


#check if update is avaliable
for i, item in data:
    #if i == "Xperia™ XA1 Ultra":
     if i == "Xperia™ XA1 Ultra":
        if item != "Will be updated to Android™ 8.0":
            launched = True
            print( item )
            print( launched )
        else:
            launched = False
            print( item )
            print( launched )

#send mail
server = smtplib.SMTP('mail.grupocdmax.com.br', 25)
server.login("admin", "teste")

msg = "Hello!" # The /n separates the message from the headers
server.sendmail("firmo@viize.com", "firmo@viize.com", msg)