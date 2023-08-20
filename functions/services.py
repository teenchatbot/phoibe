# this outlines stuff like alert



class services:
    def alert():
        with open("syscrit/people/alert.txt", "r") as file:
            lines = file.read()
        return lines
