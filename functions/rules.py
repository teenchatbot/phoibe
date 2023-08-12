

class rules:
    def read():
        with open("rules.txt", "r") as file:
            rules = str(file.read())
            rules = rules.split('\n')
            return rules
    def srule(rule):
        with open("rules.txt", "r") as file:
            line = file.readlines()
            return str(line[rule - 1])
