import json


class ucal:
    def check(username, commandLevel):
        with open("json-files/ucal.json", "r") as file:
            data = json.load(file)
            if username not in data:
                data['people'][username] = 0
                with open("json-files/ucal.json", "w") as file:
                    json.dump(data, file, indent=4)
            if username in data:
                level = data['people'][username]
                if level >= commandLevel:
                    return True
                else:
                    return False
    def raiseLevel(username, levels):
        with open("json-files/ucal.json", "r") as file:
            data = json.load(file)
            data['people'][username] = data['people'][username] + levels
            with open("json-files/ucal.json", "w") as file:
                json.dump(data, file, indent=4)
