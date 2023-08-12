import datetime
import internal



class logs:
    def writeToLogs(message):
        now1 = datetime.datetime.now()
        time = now1.strftime('%Y-%m-%d %H:%M:%S')
        date = now1.strftime('%Y-%m-%d')
        file = "./logs/" + date + ".log"
        hashpath = "./hashes/" + date + ".hash"
        with open(file, "a+") as f:
            f.write(str(time) + " - " + "message" + "\n")
            internal.hashes.hashfile(file, hashpath)
