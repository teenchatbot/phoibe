import json


class ucal:
    def check(username, commandLevel):
        with open("json-files/ucal.json", "r") as file:
            data = json.load(file)
            if username not in data.keys():
                data[username] = 0
                with open("json-files/ucal.json", "w") as file:
                    json.dump(data, file, indent=4)
            if username in data:
                level = data[username]
                if int(level) >= commandLevel:
                    return True
                else:
                    return False
    def raiseLevel(username, levels):
        with open("json-files/ucal.json", "r") as file:
            data = json.load(file)
            data[username] = data[username] + int(levels)
            with open("json-files/ucal.json", "w") as file:
                json.dump(data, file, indent=4)
    def add(username):
        with open("json-files/ucal.json") as file:
            data = json.load(file)
            if username not in data.keys():
                data[username] = 0
                with open("json-files/ucal.json", "w") as file:
                    json.dump(data, file, indent=4)
