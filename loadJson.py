import json, requests,  xlwt
from datetime import datetime
    
#get location info
rLocation = requests.get(url='https://shiftstestapi.firebaseio.com/locations.json')
dataLocation = json.loads(rLocation.content.decode())

#get user info
rUser = requests.get(url='https://shiftstestapi.firebaseio.com/users.json')
dataUser = json.loads(rUser.content.decode())

#get time punche
rTimePunche = requests.get(url='https://shiftstestapi.firebaseio.com/timePunches.json')
dataTimePunche = json.loads(rTimePunche.content.decode())
#------------------------------------------------------------------------------

#location
#print(type(dataLocation))
#print(len(dataLocation))
#print(dataLocation)
#------------------------------------------------------------------------------

#user info
#print(dataUser['25753'])
#print (len(dataUser['25753']))

#print(dataUser['25753']['517135']['firstName'])

#for user in dataUser['25753']:
#    print (dataUser['25753'][user]['firstName'] )

#------------------------------------------------------------------------------
data = []
#time punche
for timePunche in dataTimePunche:

    #checks if imput data is empty amd skip current time punche entry
    if ( dataTimePunche[timePunche]['clockedOut'] or dataTimePunche[timePunche]['clockedIn'] ) == '0000-00-00 00:00:00':
        continue
    
    clockedOut = datetime.strptime(dataTimePunche[timePunche]['clockedOut'], "%Y-%m-%d %H:%M:%S")
    clockedIn = datetime.strptime(dataTimePunche[timePunche]['clockedIn'], "%Y-%m-%d %H:%M:%S")
    workedTime = clockedOut - clockedIn


    data.append([dataTimePunche[timePunche]['userId'], dataTimePunche[timePunche]['clockedIn'], dataTimePunche[timePunche]['clockedOut'], workedTime.total_seconds()/60])

    #print(data)

#write to excel
wb = xlwt.Workbook()
ws = wb.add_sheet("timePunche.xls")
for rownum, sublist in enumerate(data):
    for colnum, value in enumerate(sublist):
        ws.write(rownum, colnum, value)
wb.save("timePunche.xls")