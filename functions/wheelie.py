import json

class wheelie:
    def wheelie(command):
        with open("json-files/manual.json", "r") as manfile:
            try:
                man = json.load(manfile)
                name = man[command]["name"]
                desc = man[command]["description"]
                usage = man[command]["usage"]
                return name, desc, usage
            except:
                return "that is not a command, please try again"
