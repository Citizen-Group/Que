import sys

import Person


class menu:
    def __init__(self, queue, database):
        self.queue = queue
        self.database = database

    def screen1(self):
        print("************Citizen Queuing System**************")
        print()

        choice = input(
            """
            1: Add Person to Queue
            2: Remove Person From Queue
            3: View The Queue 
            4: Call up user
            5: View Local Queue
            6: Check in user
            7: Update user info
            0: Close

            Please enter your choice: """)

        if choice == "1":

            self.addUser()
        elif choice == "2":

            self.removeUser()
        elif choice == "3":
            self.displayQueue()
        elif choice == "4":
            self.callUpUser()
        elif choice == "5":
            self.displayLocalQueue()
        elif choice == "6":
            self.checkIn()
        elif choice == "7":
            self.updateUser()
        elif choice == "0":
            sys.exit()
        else:
            print("You must only select 1-4")
            print("Please try again")

            self.screen1()


    def addUser(self,bioID= None):
        name = input("What is the user's name ")
        reason = input("Reason for visit ")
        waitTime = self.database.estimateWaitTime()
        position = 0
        if self.database.isEmpty():
            position = 1
        else:

            position = self.database.findLastPosition()



        if bioID is not None:
            user = Person.person(name,reason,position,waitTime,uniqueID=bioID)
        else:
            user = Person.person(name,reason,position,waitTime)

        self.queue.addperson(user)
        print("Add Complete")

        self.screen1()



    def removeUser(self):
        print(self.queue)
        id = input("Please select the id of the user you want to remove ")
        self.database.updateWaitTime(id)
        self.queue.removeperson(id)

        self.screen1()


    def callUpUser(self):
        print(self.queue)
        id = input("Please select the id of the user you want to call up ")
        if self.queue.getName(id) is not None:

            print("could " + self.queue.getName(id) + " please come up to the desk")
        else:
            print("User not found")
    def displayQueue(self):
        self.database.viewDataBase()

        self.screen1()
    def displayLocalQueue(self):
        print(self.queue)

        self.screen1()

    def checkIn(self):
        user = self.database.callUp()
        print("Now calling: " + str(user["_id"]))
        self.queue.updateQueue()


        self.screen1()

    def updateUser(self):
        id = input("Please enter the ID of the user you want to change")
        spot = input("Please enter what number in line you would like to set him to")
        self.database.changePosition(id,spot)
        self.queue.updateQueue()

        self.screen1()