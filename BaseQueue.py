import Person


class BaseQueue():

    def __init__(self, database):
        self.items = []
        self.database = database
        self.updateQueue()

    def __repr__(self):
        stringrep = ""
        for i in self.items:
            stringrep = stringrep + str(i.userID) + ": " + i.name + ", "
        return stringrep

    def isEmpty(self):
        return self.items == []

    def updateQueue(self):

        if self.database.isEmpty():
            print("Creating new queue")
            return None
        else:
            for i in self.database.toList():
                self.items.append(Person.person.fromJSON(i))

    def addPerson(self, user):
        self.items.append(user)
        self.database.addtoqueue(user)

    def removePerson(self, id):
        for i in self.items:
            print(i.userID)
            if str(i.userID) == str(id):
                user = i
                self.database.removefromqueue(user)
                self.items.remove(user)
                return None

        print("User not found")

    def removeById(self, id):
        for i in self.items:
            if i.userID == id:
                user = i
                self.items.remove(user)
        else:
            print("ID not found")

    def size(self):
        return len(self.items)

    def findID(self, item):
        for i in self.items:
            if self.items[i].isInstance(Person):
                if self.items[i] == item:
                    return True
        return False

    def getPositionInQueue(self, item):
        if self.findID(item) == True:
            return self.items.index(item)
        else:
            return None

    def getPersonByID(self, id):
        for i in self.items:
            if self.items[i].isInstance(Person):
                if self.items[i].userID == id:
                    return self.items[i]
        return None
