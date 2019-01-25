import json, requests, xlwt, time
from datetime import datetime

#load data from json files and print computed output
def loadDataProcessAndPrint():

    #load data from json
    #get location info
    rLocation = requests.get(url='https://shiftstestapi.firebaseio.com/locations.json')
    dataLocation = json.loads(rLocation.content.decode())

    #get user info
    rUser = requests.get(url='https://shiftstestapi.firebaseio.com/users.json')
    dataUser = json.loads(rUser.content.decode())

    #get time punche
    rTimePunche = requests.get(url='https://shiftstestapi.firebaseio.com/timePunches.json')
    dataTimePunche = json.loads(rTimePunche.content.decode())

    #create dictionay with extracted info
    data = []
    #time punche
    for timePunche in dataTimePunche:

        #checks if imput data is empty amd skip current time punche entry
        if ( dataTimePunche[timePunche]['clockedOut'] or dataTimePunche[timePunche]['clockedIn'] ) == '0000-00-00 00:00:00':
            continue
        
        clockedOut = datetime.strptime(dataTimePunche[timePunche]['clockedOut'], "%Y-%m-%d %H:%M:%S")
        clockedIn = datetime.strptime(dataTimePunche[timePunche]['clockedIn'], "%Y-%m-%d %H:%M:%S")
        workedTime = clockedOut - clockedIn

        data.append([dataTimePunche[timePunche]['userId'],      #userID
                    dataTimePunche[timePunche]['clockedIn'],   #clockedIn
                    dataTimePunche[timePunche]['clockedOut'],  #clockedOut
                    clockedOut.weekday(),                      #week day
                    clockedOut.isocalendar()[1],               #week number
                    workedTime.total_seconds()/60],            #workedTime
                    )

    #export data
    expData = []
    weekNum = 1

    workedHours = 0
    workedTimeWeek = 0
    workedTimeWeekEnd = 0
    workedOvertimeWeek = 0
    workedOvertimeWeekEnd = 0

    for user in dataUser['25753']:
        for weekNum in range(52):
            i = 0
            weekNum += 1
            for item in data:
                if (data[i][0] == dataUser['25753'][user]['id']) and (data[i][4] == weekNum):
                    if (data[i][3] < 5):    #if workday is on the week
                        workedTimeWeek += data[i][5]
                        if (workedTimeWeek > 480): 
                            workedOvertimeWeek += workedTimeWeek - 480
                    else:
                        workedOvertimeWeekEnd += data[i][5]
                    workedHours = workedTimeWeek + workedTimeWeekEnd
                i += 1

        expData.append([    dataUser['25753'][user]['firstName'],
                            dataUser['25753'][user]['lastName'],
                            workedHours,
                            workedTimeWeek,
                            workedTimeWeekEnd,
                            workedOvertimeWeek,
                            workedOvertimeWeekEnd,
                            dataUser['25753'][user]['photo'],
                        ])


        print(expData)
#------------------------------------------------------------------------------

#write to excel
def writeToExcel():
    wb = xlwt.Workbook()
    ws = wb.add_sheet("timePunche.xls")
    for rownum, sublist in enumerate(data):
        for colnum, value in enumerate(sublist):
            ws.write(rownum, colnum, value)
    wb.save("timePunche.xls")
#------------------------------------------------------------------------------

#main function
def main():
    loadDataProcessAndPrint()
    #writeToExcel()
#------------------------------------------------------------------------------

#call main
main()