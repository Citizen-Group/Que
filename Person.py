from services.citizenIDInterface import CitizenIDInterface as interfacer
class person:
    _lastID = 0
    def __init__(self,name,reason,position,waitTime,userID= None, uniqueID = None, serviceData=None):
        self.userID = userID
        self.waitTime = waitTime
        self.reason = reason
        self.serviceData = serviceData
        self.position = position
        idConverter = interfacer()
        self.uniqueID= idConverter.getUUIDviaBIO(uniqueID)
        if userID == None:
            self.userID = person._lastID
            person._lastID += 1

        self.name = name


    @classmethod

    def fromJSON(cls,Json):
        if person._lastID <= int(Json["_id"]):
            person._lastID = int(Json["_id"]) + 1
        return cls( Json["name:"],Json["reason:"],Json["position:"],Json["waitTime:"],Json["_id"],Json["uniqueID:"],Json["serviceData:"])



