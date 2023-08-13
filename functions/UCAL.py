import json


class ucal:
    def check(username, commandLevel):
        with open("json-files/ucal.json", "r") as file:
            data = json.load(file)
            if username not in data:
                data[username] = 0
                with open("json-files/ucal.json", "w") as file:
                    json.dump(data, file, indent=4)
            if username in data:
                level = data[username]
                if level >= commandLevel:
                    return True
                else:
                    return False
