import os

API_ID = API_ID = 22170620

API_HASH = os.environ.get("API_HASH", "8c15defa8633511dd14b19b5770cb9e8)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7146439451:AAHWUl57EYfvc1GpSuSjoiohxl15JW2zxtY)

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5931133686)

LOG = -1002085420480

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5721835845").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
