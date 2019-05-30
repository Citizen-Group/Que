import sys
import time

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
            4: View The Database
            5: Close

            Please enter your choice: """)

        if choice == "1":

            self.addUser()
        elif choice == "2":

            self.removeUser()
        elif choice == "3":
            self.displayQueue()
        elif choice == "4":
            self.displayDatabase()
        elif choice == "5":
            sys.exit()
        else:
            print("You must only select 1-4")
            print("Please try again")
            time.sleep(3)
            self.screen1()


    def addUser(self):
        name = input("What is the user's name ")

        user = Person.person(name)

        self.queue.addperson(user)
        print("Add Complete")
        time.sleep(2)
        self.screen1()



    def removeUser(self):
        print(self.queue)
        id = input("Please select the id of the user you want to remove ")
        self.queue.removeperson(id)
        time.sleep(2)
        self.screen1()


    def displayDatabase(self):
        self.database.viewDataBase()
        time.sleep(2)
        self.screen1()

    def displayQueue(self):
        print(self.queue)
        time.sleep(2)
        self.screen1()