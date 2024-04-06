import json


class prestige:
    def prestige(username, message):
        with open("json-files/prestige.json", "r") as file:
            data = json.load(file)
        if username not in data.keys():
            data[username] = 1
            with open("json-files/prestige.json", "w") as file:
                json.dump(data, file, indent=4)
        if username in data.keys():
            data[username] = data[username] + 1
            with open("json-files/prestige.json", "w") as file:
                json.dump(data, file, indent=4)

        words = message.split(" ")
        for word in words:
            if word in data.keys():
                data[word] = data[word] + 1
                with open("json-files/prestige.json", "w") as file:
                    json.dump(data, file, indent=4)


    def getPrestige(username):
        with open("json-files/prestige.json", "r") as file:
            data = json.load(file)
        if username in data.keys():
            prestigeLevel = data[username]
        else:
            rankString = "Your username was not found on the prestige list, please chat some more so you can be on it"
        if prestigeLevel < 100:
            rankString = "Your prestige level is: " + str(prestigeLevel) + ", putting you in Wood"
        if prestigeLevel > 100 and prestigeLevel < 200:
            rankString = "Your prestige level is: " + str(prestigeLevel) + ", putting you in Stone"
        if prestigeLevel >= 200 and prestigeLevel < 300:
            rankString = "Your prestige level is: " + str(prestigeLevel) + ", putting you in Metal"
        if prestigeLevel >= 300 and prestigeLevel < 400:
            rankString = "Your prestige level is: " + str(prestigeLevel) + ", putting you in Diamond"
        if prestigeLevel >= 400 and prestigeLevel < 600:
            rankString = "Your prestige level is: " + str(prestigeLevel) + ", putting you in Platinum"
        if prestigeLevel >= 600 and prestigeLevel < 1000:
            rankString = "your prestige level is: " + str(prestigeLevel) + ", putting you in Ruby"
        if prestigeLevel >= 1000 and prestigeLevel < 5000:
            rankString = "your prestige level is: " + str(prestigeLevel) + ", putting you in Notable People"
        if prestigeLevel >= 5000 and prestigeLevel < 10000:
            rankString = "your prestige level is: " + str(prestigeLevel) + ", putting you in Famous"
        if prestigeLevel >= 10000:
            rankString = "Your prestige level is off the charts at: " + str(prestigeLevel) + ", putting you in Legend"
        return rankString

