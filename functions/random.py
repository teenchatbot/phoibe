import json
import random



class entrances:
    def entrance():
        with open("json-files/settings.json", "r") as file:
            data = json.load(file)
            entrances = data['core']['entrances']
            return random.choice(entrances)
class cuss:
    def cuss():
        with open("json-files/random.json", "r") as file:
            data = json.load(file)
            words = data['cuss_words']
            return random.choice(words)
class insults:
    def insult():
        with open("json-files/random.json", "r") as file:
            data = json.load(file)
            insults = data['insults']
            return random.choice(insults)
class drink:
    def drink(username):
        with open("json-files/random.json", "r") as file:
            data = json.load(file)
            drinks = data['drinks']
            return random.choice(drinks) + " " + username
class joke:
    def joke():
        with open("json-files/random.json") as file:
            data = json.load(file)
            jokes = data['jokes']
            return random.choice(jokes)
