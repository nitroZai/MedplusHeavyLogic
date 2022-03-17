import csv
import time
import random

class Vehicle(object):

    def __init__(self, length, width, vType) -> None:
        self.length = length
        self.width = width
        self.vType = vType

    def getArea(self):
        return (self.length * self.width)

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width
    def getvType(self):
        return self.vType

class Bike(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class Car(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class Bus(Vehicle):
    def __init__(self, length, width, vType) -> None:
        super().__init__(length, width, vType)

class ParkingLot(object):

    lotLength = 100
    lotWidth = 10
    lotArea = lotLength * lotWidth

    dictionArea = {
        'A':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'B':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'C':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        },
        'D':{
            'totalArea': lotArea,
            'bus': lotArea * 0.1,
            'car': lotArea * 0.6,
            'bike':lotArea * 0.3,
        }
    }

    dictionVehicleAllocation = {

        'A': {},
        'B': {},
        'C': {},
        'D': {}

    }

    def __init__(self, length, width) -> None:
        self.lotLength = length
        self.lotWidth = width        

    def setLotArea(self):
        self.lotArea = self.lotLength * self.lotWidth
    
    def getLotArea(self):
        self.lotArea = self.lotLength * self.lotWidth
        return self.lotArea
        
        
if __name__ == '__main__':
    parkingLot = ParkingLot(100,10)
    parkingLot.setLotArea()
    print(parkingLot.getLotArea())

    csvPower = open('parkingLotData.csv','w', newline='')
    csvWrite = csv.writer(csvPower, delimiter=',')
    csvWrite.writerow(['Serial', 'Vehicle Number', 'In Time', 'Out Time', 'Checkout Amount'])
    serials = ['A', 'B', 'C', 'D'] 

    while True:
        print("-------------------------------")
        print("|                             |")
        print("|  Welcome to MP Parking Lot  |")
        print("|                             |")
        print("-------------------------------")

        print("Our Services:")
        print("1. Allot space for your vehicle")
        print("2. De-Allocate your Vehicle")
        print("3. Exit")
        choice = int(input("Enter your Choice? "))

        if choice == 1:
            
            choiceVehicle = input("What's the type of your vehicle bike/car/bus? ")

            if choiceVehicle == "bike":
                bObject = Bike(4, 2, "bike")
                bObjectArea = bObject.getArea()
                #print(bObjectArea)
                bOjectName = input("Enter the Bike Number")

                for x in serials:
                    print(parkingLot.dictionArea[x][choiceVehicle])
                    
                    if bObjectArea >= parkingLot.dictionArea['D'][choiceVehicle]:
                        print("We are Out of Space, Visit us again!")
                    
                    if bObjectArea <= parkingLot.dictionArea[x][choiceVehicle]:
                        parkingLot.dictionArea[x][choiceVehicle] -= bObjectArea
                        inTime = random.randint(1,24)
                        parkingLot.dictionVehicleAllocation[x][bOjectName] = inTime
                        print(f"{bObject.vType} with Number {bOjectName} is parked in Serial: {x}!")
                        break
                    else:
                        continue


            elif choiceVehicle == "car":
                cObject = Car(5,4, "car")
                cObjectArea = cObject.getArea()
                cOjectName = input("Enter the Car Number")

                for x in serials:
                    if cObjectArea >= parkingLot.dictionArea['D'][choiceVehicle]:
                        print("We are Out of Space, Visit us again!")

                    if cObjectArea <= parkingLot.dictionArea[x][choiceVehicle]:
                        parkingLot.dictionArea[x][choiceVehicle] -= cObjectArea
                        inTime = random.randint(1,24)
                        parkingLot.dictionVehicleAllocation[x][cOjectName] = inTime
                        print(f"{cObject.vType} with Number {cOjectName} is parked in Serial: {x}!")
                        break
                    else:
                        continue

            elif choiceVehicle == "bus":
                busObject = Bus(10,4,"bus")
                busObjectArea = busObject.getArea()
                busOjectName = input("Enter the Bus Number")

                for x in serials:
                    if busObjectArea >= parkingLot.dictionArea['D'][choiceVehicle]:
                        print("We are Out of Space, Visit us again!")
                        break

                    if busObjectArea <= parkingLot.dictionArea[x][choiceVehicle]:
                        parkingLot.dictionArea[x][choiceVehicle] -= busObjectArea
                        inTime = random.randint(1,24)
                        parkingLot.dictionVehicleAllocation[x][busOjectName] = inTime
                        print(f"{busObject.vType} with Number {busOjectName} is parked in Serial: {x}!")
                        print(parkingLot.dictionVehicleAllocation.items())
                        break
                    else:
                        continue

        elif choice == 2:
            
            flag = 0
            vehicleNumber = input("Enter your VehicleNumber")
            
            for keys, values in parkingLot.dictionVehicleAllocation.items():
                for xkeys, xValues in values.items():
                    
                    if vehicleNumber == xkeys:
                        
                        flag = 1

                        tempInTime = parkingLot.dictionVehicleAllocation[keys][xkeys]
                        outTime = random.randint(1,24)
                        if tempInTime == outTime:
                            outTime = random.randint(1,24)


                        counter = 0
                        tempOutTime = outTime
                        tempTempInTime = tempInTime
                        if tempOutTime < tempTempInTime:
                            
                            while True:
                                if tempOutTime == 24:
                                    break
                                tempOutTime += 1
                                counter += 1
                            
                            duration = (counter + outTime) * 60
                        else:
                            duration = abs(outTime - tempInTime) * 60

                        print("InTime", tempInTime)
                        print("OutTime", outTime)
                        parkingLot.dictionVehicleAllocation[keys].pop(xkeys)

                        amountPayable = 0

                        print(parkingLot.dictionVehicleAllocation)

                        if duration >= 30 and duration <= 60:
                            amountPayable += 20
                        elif duration >= 60 and duration <= 600:
                            amountPayable = (duration // 60) * 10
                        elif duration > 600:
                            amountPayable = (duration // 60) * 5

                        csvWrite.writerow([keys ,vehicleNumber, tempInTime, outTime, amountPayable])
                        break
            
            
            if flag == 0:
                print("The entered Car Number isn't Valid")
            else:
                print("Thanks for Visiting us!")
                print("Amount payable: {}".format(amountPayable))

        else: 
            break

