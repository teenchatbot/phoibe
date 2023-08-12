import json

class fight:
    def fight(username1, username2):
        basescore1 = 500
        basescore2 = 500
        #lowecase both of the usernames
        user1 = username1.lower()
        user2 = username2.lower()
        #open the values file
        with open("json-files/values.json", "r") as file:
            data = json.load(file)
        #check the usernames against the values to produce a score
        for letter in user1:
            for shit in data['values']:
                if letter == shit:
                    basescore1 = basescore1 + data['values'][shit]
            basescore1 = basescore1 * 100
        for letter in user2:
            for shit in data['values']:
                if letter == shit:
                    basescore2 = basescore2 + data['values'][shit]
            basescore2 = basescore2 * 100
        if basescore1 > basescore2:
            return username1 + " won this fight"
        if basescore1 < basescore2:
            return username2 + " won this fight"
        else:
            return "they tied"

class messages:
    def custom(username):
        with open('json-files/cMessages.json', 'r') as f:
            data = json.load(f)
        if username in data['custom_messages']:
            return data['custom_messages'][username]
        else:
            return username + " what?"
