from random import randint

class Train:
    def __init__(slf, trainNo):## here we change the self into the slf function 
        slf.trainNo = trainNo


    def book(anni, fro, to):
        print(f"Ticket is booked in train no: {anni.trainNo} from {fro} to {to}")## here we change the self into anni 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(1234321)
t.book("rampura", "delhi")
t.getStatus()
t.getFare("rampura", "delhi")
## but after that the resultant was samem as the self function