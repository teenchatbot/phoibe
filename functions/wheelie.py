import json

class wheelie:
    def wheelie(command):
        with open("json-files/manual.json", "r") as manfile:
            man = json.load(manfile)
            name = man[command]["name"]
            desc = man[command]["description"]
            usage = man[command]["usage"]
        return name, desc, usage
