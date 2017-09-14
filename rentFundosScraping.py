import requests 
from bs4 import BeautifulSoup
import xlwt

#banco do brasil
url = "http://www37.bb.com.br/portalbb/tabelaRentabilidade/rentabilidade/gfi7,802,9085,9089,8.bbx?tipo=2&nivel=1000"

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

print(data)

#write to excel
wb = xlwt.Workbook()
ws = wb.add_sheet("fundosBB.xls")
for rownum, sublist in enumerate(data):
    for colnum, value in enumerate(sublist):
        ws.write(rownum, colnum, value)
wb.save("fundosBB.xls")