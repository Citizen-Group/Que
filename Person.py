class person:
    _lastID = 0
    def __init__(self,name,userID= None,):
        self.userID = userID
        if userID == None:
            self.userID = person._lastID
            person._lastID += 1

        self.name = name


    @classmethod

    def fromJSON(cls,Json):
        if person._lastID <= int(Json["_id"]):
            person._lastID = int(Json["_id"]) + 1
        return cls( Json["name:"],Json["_id"])



