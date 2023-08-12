



class backlog:
    def assign(username):
        try:
            if username != "read":
                return "ok, " + username + " has been reported"
        except:
            return "an error has occured"
    def read():
        usernames = open("./syscrit/people/backlog.txt", "r")
        usernames = str(usernames.read())
        usernames = usernames.replace("\n", " ")
        return usernames
class blacklist:
    def check(username):
        blacklist = open("./syscrit/people/blacklist.txt", "r")
        blacklist = str(blacklist.read)
        true_blacklist = blacklist.split("\n")
        if username in true_blacklist:
            return True
        else:
            return False
class minimods:
    def mMods():
        with open("./syscrit/people/minimods.txt") as f:
            lin = f.read()
            lines = lin.split("\n")
            return lines
    def test():
        return "your test has been successful"
class regUsers:
    def check(username):
        with open("./syscrit/people/regusers.txt", "r") as f:
            lin = str(f.read())
            users = lin.split("\n")
            if username in users:
                return True
            else:
                return False
