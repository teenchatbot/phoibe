



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
    def check():
        blacklist = open("./syscrit/people/blacklist.txt", "r")
        blacklist = str(blacklist.read)
        true_blacklist = blacklist.split("\n")
        return true_blacklist
