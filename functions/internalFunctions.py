import datetime
# TODO: going to have to import the hash functions to do this


class logs:
    def writeToLogs(message):
        now1 = datetime.datetime.now()
        time = now1.strftime('%Y-%m-%d %H:%M:%S')
        date = now1.strftime('%Y-%m-%d')
        file = "./logs/" + date + ".log"
        with open(file, "a+") as f:
            f.write(str(time) + " - " + "message" + "\n")
