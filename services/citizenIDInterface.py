from services.citizenIDFakeRemoteHost import CitizenIDRemoteHost as remoteHost

# Interface to allow access to the Remote Citizen Card Server

class CitizenIDInterface():
    ## Helper Functions
    # Gets a Biometic from the database for testing
    def getBiometicFromDB(self, num):
        # if num is -1 then get random else get "num" user
        pass

    # Gets a Card from the database for testing
    def getCardFromDB(self, num):
        # if num is -1 then get random else get "num" user
        pass

    def getUUIDviaBIO(self, BioMetricPayload):
       pass

    def getUUIDviaCARD(self, CCardID):
       pass

    def createCitizenFromCard (self):
        pass
    
    def createCitizenFromBio (self):
        pass