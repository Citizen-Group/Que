import Person


class BaseQueue():

    def __init__(self,database):
        self.items = []
        self.database = database
        self.updateQueue()

    def __repr__(self):
        stringrep = ""
        for i in self.items:

            stringrep = stringrep + str(i.userID) +": " + i.name + ", " + "Position: " + str(i.position) + "\n"
        return stringrep

    def isEmpty(self):
        return self.items == []

    def updateQueue(self):
            itemNew = []
            if self.database.isEmpty():
                print("Creating new queue")
                return None
            else:
                for i in self.database.toList():
                    itemNew.append(Person.person.fromJSON(i))
            self.items = itemNew


    def addperson(self, user):
        self.items.append(user)
        self.database.addtoqueue(user)

    def getName(self, id):
        for i in self.items:

            if str(i.userID) == str(id):
                return i.name
    def removeperson(self,id):
        for i in self.items:

            if str(i.userID) == str(id):
                user = i
                self.database.removefromqueue(user)
                self.items.remove(user)
                return None

        print("User not found")


    def removebyid(self,id):
        for i in self.items:
            if i.userID == id:
                user = i
                self.items.remove(user)
        else:
            print("ID not found")


    def size(self):
        return len(self.items)

    def findID(self,item):
        for i in self.items:
            if self.items[i].isInstance(Person):
                if self.items[i] == item:
                    return True
        return False

    def getPositionInQueue(self,item):
        if self.findID(item) == True:
            return self.items.index(item)
        else:
            return None

    def getPersonByID(self,id):
        for i in self.items:
            if self.items[i].isInstance(Person):
                if self.items[i].userID == id:
                    return self.items[i]
        return None




