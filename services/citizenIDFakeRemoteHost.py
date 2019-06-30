import json
import uuid

## Mockup of the CID Service Schema

# ID        - Internal ID for record keeping (Never Changes)
# CUUID     - True Citizen ID (Pirvate, Changed for secuirty reasons) (Think as a guarded private Key)
# CID       - Your Citizen ID (Public, Semi Fixed) (Think of it as a protected public key)

# CARD      - Object of Cards for tracking history
# CARD.ID   - Unique Card ID (Semi Private, Can be deactivated for secuirty reasons and lost cards)  
# CARD.isActive     - Unique Card ID (Semi Private, Can be deactivated for secuirty reasons and lost cards)  

# BIOMETRIC         - OBject of "type, payload" (Private, Can be updated or Deleted)
# BIOMETRIC.TYPE    - ENUM of 'types of biometic devices'. Unique. Denotes how we should parse the data 
# BIOMETRIC.PAYLOAD - The data payload for this biometic type


## Linked tables

# USER   - ID links to the USER table for client information
# TRANSACTIONS - ID Links to 
# KEYS - Public ID codes for various needs


# Provides a simulated Citizen Card Remote Server

class CitizenIDRemoteHost():
    # Starting DB Size
    DATABASE_SIZE = 20
    
    # ENUM of Biometric types, incase we have more then one input device/style
    BIO_TYPE = {
        "FINGER": 0
    }

    # Array of fake users. ID is the key value here
    database = {}

    #Encryp/Decyrp Seed
    salt = 5

    # Helper function to generate BIO Code
    def generateBio(self, type):
        x = 20 + type
        x += uuid.uuid4()
        x += uuid.uuid4()
        x += uuid.uuid4()
        return str(x)


    # Helper function to generate UUID's
    def generateUUID(self, seed, length):
        x = uuid.uuid4()
        return str(x)[:length]

    
    def __init__(self):
        pass
    
    def returnDBSize(self):
        return self.DATABASE_SIZE

    # Seed users in th e database
    def initDatabase(self):
        # For each nummber in range to 20
        for x in range(self.DATABASE_SIZE):
            # Create a user randomly for the fake database. ID is the key
            self.database[x] = {
                "CUUID" : self.generateUUID(x, 5),
                "CID" : self.generateUUID(x, 8),
                "CARD" : { 
                    "ID": self.generateUUID(x, 8),
                    "isActive": True
                },
                "BIOMETRIC" : { 
                    "TYPE": self.BIO_TYPE["FINGER"],
                    "PAYLOAD": self.generateBio(self.BIO_TYPE["FINGER"])
                }
            }
            pass
        

    # Authorizes the connection
    def auth(self, query):
        if (query == "poop"):
            return True
        else: 
            return False

    # Encryptor
    def encrypt(self, payload):
        return "poop"

    # Decryptor
    def decrypt(self, payload):
        return "poop"

    # Fake Database Tools
    def getCardByID(self, ID):
        # Needs check for ID greater then DATABASE_SIZE and for no founds
        return self.database[ID]["CARD"]

    def getBioByID(self, ID):
        # Needs check for ID greater then DATABASE_SIZE and for no founds
        return self.database[ID]["BIOMETRIC"]

    def getCIDByCard(self, cardID):
        for element in self.database:
            if (element["CARD"]["isActive"] == True):
                if (element["CARD"]["ID"] == cardID):
                    return element["CID"]
            pass
        return -1
    
    def getCIDByBio(self, bioType, payload):
        for element in self.database:
            if (element["BIOMETRICS"]["TYPE"] == bioType):
                if (element["BIOMETRICS"]["PAYLOAD"] == payload):
                    return element["CID"]
            pass
        return -1
    
    # Takes a product type (Biometric, Card) and a payload/ID to look for match on DB
    # Returns {
    #   Code
    #   Message: If code != 200 then message is error code, else it is CID
    # }
    def queryForCID(self, product, payload, bioType = -1):
        # Helper function for replies
        def passed(payload):
            return {
                "code": 200, 
                "message": payload
            }

        def failed():
            return {
                "code": 300, 
                "message": "Unabled to find"
            }

        # Later on the real server this will be a lookup table
        # that matches product ID to executing function, with no If's
        if (product == "QUE-BIO"):
            x = self.getCIDByBio(bioType, payload)

            if (x >= 0):
                return passed(x)
            else:
                return failed()
        elif (product == "QUE-CARD"):
            x = self.getCIDByCard(payload)

            if (x >= 0):
                return passed(x)
            else:
                return failed()

        else:
            return {
                "code":300, 
                "message": "Remote Server does not support '" + product + "' product type"
            }

    # Fake Web Paths
    # Querys the Internal database to get the Citizen UUID of the 
    def UUIDRequest(self, auth, req):

        local_returnedUUID = {}

        # Check Auth
        if (not self.auth(auth)):
            return {
                "code":300, 
                "message": "Remote Server rejected your authorization"
            }

        # We only support QUE at this time 
        #   QUE-Card is the same as the Citizen Card, but for production purposes. 
        #   I don't want loosely handed out Citizen Cards, to be Citizens. 
        #   It would pollute the system. This will likely change as things progress.

        if (req["product"].lower() == "que-card"):
            # Needs defensive checks for missing values
            local_returnedUUID = self.queryForCID(req["product"].lower(), req["payload"])
        elif (req["product"].lower() == "que-bio"):
            # Needs defensive checks for missing values
            local_returnedUUID = self.queryForCID(req["product"].lower(), req["payload"], self.BIO_TYPE[req["biotype"]])
        else:
            return {
                "code":300, 
                "message": "Remote Server does not support '" + req["product"] + "' product type"
            }

        if (local_returnedUUID == {}):
            return {
                "code": 300, 
                "message": "Fatal error. Database failed to respond"
            }
        elif (local_returnedUUID["code"] != "200"):
            return {
                "code": local_returnedUUID["code"], 
                "message": local_returnedUUID["message"]
            }

        return {
            "code":200, 
            "message": local_returnedUUID["message"]
        }

        