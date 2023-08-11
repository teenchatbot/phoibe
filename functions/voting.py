import json



class voice:
    def vote(username, vote):
        with open("./json-files/voting.json", "r") as f:
            data = json.load(f)
        if vote == "yay" or "Yay":
            # ^ checked if the vote was yay
            if username in data['voice']['yay']:
                return "you have already voted"
            else:
                with open("./json-files/voting.json", "w") as f:
                    data = json.load(f)
                    data = data['voice']['yay'].append(username)
                    json.dump(data, f, indent=4)
        elif vote == "nay" or "Nay":
            if username in data['voice']['nay']:
                return "you have already voted"
            else:
                with open("./json-files/voting.json", "w") as f:
                    data = json.load(f)
                    data = data['voice']['nay'].append(username)
                    json.dump(data, f, indent=4)
    def clear():
        with open("./json-files/voting.json", "w") as f:
            data = json.load(f)
            data = data['voice']['yay'] = []
            data = data['voice']['nay'] = []
            json.dump(data, f, indent=4)
    def read():
        with open("./json-files/voting.json", "r") as f:
            data = json.load(f)
            yays = len(data['voice']['yays'])
            nays = len(data['voice']['nays'])
            return yays, nays


