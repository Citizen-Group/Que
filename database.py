from pprint import pprint

import pymongo


class database:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")

        self.db = self.client.queuesystem

        self.collection = self.db.line


    def addToQueue(self,item):
        client = {"_id": item.userID, "name:": item.name}
        x = self.collection.insert_one(client)

    def removeFromQueue(self,item):
        client = {"_id": item.userID, "name:": item.name}

        y = {"_id": item.userID}

        self.collection.delete_one(y)

    def isEmpty(self):
        return self.collection.count({}) == 0

    def updateDisplay(self):
        pass



    def toList(self):
        return self.collection.find()

    def viewDataBase(self):
        cursor = self.collection.find({})
        for document in cursor:
            pprint(document)
