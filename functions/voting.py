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
class multi:
    def issue():
        with open("./syscrit/people/issue.txt") as f:
            line = f.readline()
            return line
    def castVote(username, canidate):
        file = open("json-files/elect.json", "r")
        file2 = open("./syscrit/voting/haselected.txt", "r")
        hascast = file2.read()
        hascast = hascast.split("\n")
        data = json.load(file)
        try:
            if username not in hascast:
                data['canidates'][canidate] = data['canidates'][canidate] + 1
                with open("json-files/elect.json", "w") as f:
                    json.dump(data, f, indent=4)
                with open("./syscrit/voting/haselected.txt", "a") as f:
                    f.write(username + "\n")
            else:
                return "you have already voted silly goose"
            except:
                return "an error has occured"
    def results():
        with open("json-files/elect.json", "r") as file:
            data = json.load(file)
            data = data['canidates']
            sorted = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
            return sorted
    def ballot():
        with open("./syscrit/voting/ballot.txt", "r") as f:
            file = f.read()
            file = file.split("\n")
            return file

