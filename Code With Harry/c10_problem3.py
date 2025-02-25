"""
Write a class train which has methods to book a ticket, get status(no of seats), and get fare information
of train running under Bangladesh Railways.
"""
from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
    def getStatus(self, trainNo):
        print(f"Train No: {trainNo} is available.")
    def getFare(self):
        print(f"Fare is {randint(300, 800)} Taka with Tax.")
    def booking(self, fro, to):
        print(f"Ticket is Booked from {fro} to {to}.")
        self.getStatus(self.trainNo)
        self.getFare()

antonogor = Train(234)
antonogor.booking("Rajshahi", "Dhaka")
