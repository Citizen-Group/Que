from pprint import pprint

import pymongo


class database:

    def __init__(self):
        #Change this to where ever you are hosting the database
        connected = False
        while connected == False:
            loc = input("Please enter the database loacation or leave empty for localhost: ")

            if loc == "":
                try:
                    self.client = pymongo.MongoClient("mongodb://localhost:27017/",serverSelectionTimeoutMS=1500)
                    self.client.server_info()
                except pymongo.errors.ServerSelectionTimeoutError as err:

                    print("Connection Failed")
                else:
                    connected = True
            else:

                try:
                    self.client = pymongo.MongoClient(loc,serverSelectionTimeoutMS=1500)
                    self.client.server_info()
                except pymongo.errors.ServerSelectionTimeoutError as err:

                        print("Connection Failed")
                else:
                    connected = True


        self.db = self.client.queuesystem

        self.collection = self.db.line


    def addtoqueue(self,item):
        client = {"_id": item.userID, "name:": item.name, "reason:":item.reason, "position:": item.position,"waitTime:": item.waitTime, "uniqueID:": item.uniqueID, "serviceData:": item.serviceData }
        x = self.collection.insert_one(client)

    def removefromqueue(self,item):
        client = {"_id": item.userID, "name:": item.name, "reason:":item.reason, "position:": item.position,"waitTime:": item.waitTime,"uniqueID:": item.uniqueID,"serviceData:": item.serviceData}

        y = {"_id": item.userID}

        self.collection.delete_one(y)
    def updatePositions(self):
        for x in self.collection.find():
            print(x["position:"])
            self.collection.find_one_and_update({"_id": x["_id"]},{'$inc': {"position:": -1}})

    def callUp(self):
        x = self.collection.find_one_and_delete({"position:" : 1})
        self.updatePositions()
        return x

    def isEmpty(self):
        return self.collection.count({}) == 0

    def updateDisplay(self):
        pass

    def changePosition(self,id,spot):
        ## CHECK FOR VALID INPUTS
        if int(spot) > self.findLastPosition() - 1:
            return "Out of bounds position please try again"

        current = self.collection.find_one({"_id" : int(id)})

        if int(spot) > current["position:"]:
            for x in self.collection.find():
                if (int(spot) >= x["position:"] and x["_id"] != int(id)) and (x["position:"] > current["position:"]):
                    self.collection.update_one({"_id": x["_id"]}, {"$inc": {"position:": -1 }})
        elif int(spot) < current["position:"]:
            for x in self.collection.find():
                if (int(spot) <= x["position:"] and x["_id"] != int(id))and (x["position:"] < current["position:"]):
                    self.collection.update_one({"_id": x["_id"]}, {"$inc": {"position:": 1}})
        self.collection.update_one({"_id": int(id)}, {"$set": {"position:": int(spot)}})

    def toList(self):
        return self.collection.find()

    def findLastPosition(self):
        position = 1
        for x in self.collection.find():
            if position <= x["position:"]:
                position = x["position:"] + 1
        return position

    def estimateWaitTime(self):
        waitTime = 0
        for x in self.collection.find():
            waitTime = waitTime + 5
        return waitTime

    def updateWaitTime(self,id):
        current = self.collection.find_one({"_id": int(id)})
        for x in self.collection.find():
            if x["position:"] > current["position:"]:
                self.collection.update_one({"_id": x["_id"]}, {"$inc": {"waitTime:": -5}})



    def viewDataBase(self):
        cursor = self.collection.find({})
        for document in cursor:
            pprint(document)
