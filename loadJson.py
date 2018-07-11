import json, requests
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

#time punche
for timePunche in dataTimePunche:

    #print (dataTimePunche[timePunche]['userId'])
    #print (dataTimePunche[timePunche]['hourlyWage'])
    if (dataTimePunche[timePunche]['userId']) == 517169:
        clockedOut = datetime.strptime(dataTimePunche['517169']['clockedOut'], "%Y-%m-%d %H:%M:%S")
        clockedIn = datetime.strptime(dataTimePunche['517169']['clockedIn'], "%Y-%m-%d %H:%M:%S")
        workedTime = clockedOut - clockedIn
        print(workedTime)



