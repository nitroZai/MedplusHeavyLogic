from gc import collect
import time
import csv

def hrToMinString(str):

    strSplit = str.split(":")
    hours = int(strSplit[0])
    minutes = int(strSplit[1])

    retMinutes = hours * 60 + minutes

    return int(retMinutes)


def hrToMinInteger(inte):

    inteStr = inte.split(".")
    inteFirst = int(inteStr[0])
    inteSecond = int(inteStr[1])
    inteTotal = inteFirst * 60 + inteSecond/100 * 60

    print(inteTotal)
    return (inteTotal)


def minutesToHours(inte):
    varMin = (inte % 60)/60
    varHours = inte//60
    varTotal = varMin + varHours

    return varTotal

'''
csvData = open('employeeDailyData.csv', 'a', newline="")
csvWriteData = csv.writer(csvData, delimiter=",")
csvWriteData.writerows([

    ["10:00", "18:00", "13:00", "14:00"],
    ["11:00", "19:00", "13:00", "14:00"],
    ["12:00", "18:00", "14:00", "15:00"],
    ["11:00", "17:00", "13:00", "14:00"],
    ["12:00", "20:00", "15:00", "16:00"]

])

'''

# Part 2 | CSV Data Reading
csvData = open('employeeDailyData.csv', encoding="UTF-8")
csvReaderData = csv.reader(csvData)

employeeTableString = []
for i in csvReaderData:
    employeeTableString.append(i)

# employeeTableString = [
#     ["10:00", "18:00", "13:00", "14:00"],
#     ["11:00", "19:00", "13:00", "13:30"],
#     ["12:00", "18:00", "14:00", "14:30"],
#     ["11:00", "17:00", "13:00", "14:00"]
# ]

# Converts the String standard time to Minutes, Including the Breaks

employeeTableMinutes = []

for x in employeeTableString:

    temp = []
    for y in x:

        temp.append(hrToMinString(y))

    employeeTableMinutes.append(temp)

# print(employeeTableMinutes)

# Breaking the Array minutes into two another Arrays

breakList = []
inOutList = []

# Filling the two above Arrays with our 2D array data.

for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(2):
        temp.append(employeeTableMinutes[x][y])

    inOutList.append(temp)


for x in range(len(employeeTableMinutes)):

    temp = []
    for y in range(2, len(employeeTableMinutes[0])):
        temp.append(employeeTableMinutes[x][y])

    breakList.append(temp)

# Building the Meetings Timelines List

meetingsTimeline = []

for x in range(len(inOutList)):
    temp = []
    for y in range(1):
        temp1 = []
        temp2 = []
        temp1.append(inOutList[x][y])
        temp2.append(inOutList[x][y+1])
    temp.append(temp1)
    temp.append(breakList[x])
    temp.append(temp2)
    meetingsTimeline.append(temp)
print("The meeting timeline Intial:")
print(meetingsTimeline)

while True:

    print(" ____________________________________________")
    print("|                                            |")
    print("|                   WELCOME                  |")
    print("|                      To                    |")
    print("|         EMPLOYEE MANAGEMENT SYSTEM         |")
    print("|____________________________________________|")

    print("The employees we have:")
    print("0: Shyam")
    print("1: Aditya")
    print("2: Naga")
    print("3: Prashanth")

    print("Who all you'd want to schedule meeting with me?")
    employeeInputList = []
    employeeInputList.append(int(input("Enter the first Employee ID")))
    startCounter = 0
    while True:
        if startCounter == 0:
            employeeInputList.append(int(input("Enter the next employee ID")))
        else:
            x = int(input(
                "Enter the next employee, If you don't have any in mind enter the NUMBER 10"))
            if x != 10:
                employeeInputList.append(x)
            else:
                break
        startCounter += 1

    print("Great!, This is the IDs data you've inputted {}".format(employeeInputList))
    meetingDuration = (input(print("Now input the MEETING DURATION: ")))

    meetingDurationConverted = hrToMinInteger(meetingDuration)
    print(meetingDurationConverted)

    # Find Maximum of the In Times | Kadane's Algorithm
    maxTime = 0
    maxTimeArray = []

    for x in employeeInputList:
        for y in range(len(meetingsTimeline[x])-1):

            if y == 0:
                diff = abs(meetingsTimeline[x][y]
                           [0] - meetingsTimeline[x][y+1][0])
                if meetingDurationConverted <= diff:
                    maxTimeArray.append(meetingsTimeline[x][y][0])
                    break
            else:
                diff = abs(meetingsTimeline[x][y]
                           [1] - meetingsTimeline[x][y+1][0])
                if meetingDurationConverted <= diff:
                    maxTimeArray.append(meetingsTimeline[x][y][1])
                    break

            y += 1

        maxTime = max(maxTimeArray)
        print(maxTime)
        print(maxTimeArray)

    outMax = []
    for x in inOutList:
        outMax.append(x[1])
    largestRange = max(outMax)

    while True:
        #possi = []
        maxTimeCounter = 0
        for x in employeeInputList:
            print(x)
            for y in range(len(meetingsTimeline[x])-1):
                if y == 0:
                    if meetingsTimeline[x][y][0] <= maxTime and meetingsTimeline[x][y+1][0] >= maxTime + meetingDurationConverted:
                        maxTimeCounter += 1
                    # Can take an array of possible places to insert, If the break is removed
                        # possi.append(meetingsTimeline[x][y][0])
                else:
                    if meetingsTimeline[x][y][1] <= maxTime and meetingsTimeline[x][y+1][0] >= maxTime + meetingDurationConverted:
                        maxTimeCounter += 1
                        # possi.append(meetingsTimeline[x][y][1])

        # print(possi)

        c = 0
        if maxTimeCounter == len(employeeInputList):
            for x in employeeInputList:
                temp = []
                for y in range(1):
                    temp.append(maxTime)
                    temp.append(maxTime+meetingDurationConverted)



                meetingsTimeline[x].append(temp)
                meetingsTimeline[x].sort()
                
                updation_meet_timeStart = maxTime
                updation_meet_timeEnd  = maxTime+meetingDurationConverted
                
                if c == 0:
                    print("Meeting is booked at {} and goes on uptill {}".format(
                        minutesToHours(temp[0]), minutesToHours(temp[1])))
                c += 1
            break
        else:
            maxTime += meetingDurationConverted

        if maxTime >= largestRange:
            print("Scheduling Not Possible, Pick other duration!!")
            break

    for x in employeeInputList:
        print(meetingsTimeline[x])
    
    updation_time_employee = time.ctime()
    updation_employees_involved = employeeInputList
    
    csvWrite = open("MeetingsTimeline.csv", 'a', newline='')
    csvWriteData = csv.writer(csvWrite, delimiter=",")
    csvWriteData.writerows([
      [],
      [updation_time_employee],
      ["People Involved", "Starting Time", "Ending Time"],
      [updation_employees_involved, updation_meet_timeStart, updation_meet_timeEnd]  
    ])

    choice = input("You'd want to schedule another meeting? [Y/N]")
    if choice == "Y":
        pass
    else:
        break

    # Second Half post the break
