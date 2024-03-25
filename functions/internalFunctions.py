import datetime
from functions import internal




class logs:
    def writeToLogs(message, username="phoibe"):
        now1 = datetime.datetime.now()
        time = now1.strftime('%Y-%m-%d %H:%M:%S')
        date = now1.strftime('%Y-%m-%d')
        file = "./logs/" + date + ".log"
        with open(file, "a+") as f:
            f.write(str(time) + " - " + username + " - " + message + "\n")
            internal.hashes.hashfile(file)
