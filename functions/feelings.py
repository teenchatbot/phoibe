import json


class likes:
    def get_like(like, username):
        success = False
        bannedChars = ["'}", "']" "."]
        for char in bannedChars:
            like = like.strip(char)
        with open("json-files/likes.json", "r") as f:
            data = json.load(f)
            if username in data:
                data[username].append(like)
            else:
                data[username] = [like]
        with open("json-files/likes.json", "w") as f:
            json.dump(data, f, indent=4)

    def read_like(username):
        likeness = []
        with open("json-files/likes.json", "r") as f:
            data = json.load(f)
            if username in data:
                for thing in data[username]:
                    likeness.append(thing)
                return likeness
            else:
                return "sorry, you were not found in the file"


class hates:
    def get_hate(like, username):
        success = False
        bannedChars = ["'}", "']" "."]
        for char in bannedChars:
            like = like.strip(char)
        with open("json-files/hate.json", "r") as f:
            data = json.load(f)
            if username in data:
                data[username].append(like)
                success = True
                return success
            else:
                data[username] = [like]
                success = True
                return success
        with open("json-files/hate.json", "w") as f:
            json.dump(data, f, indent=4)

    def read_like(username):
        likeness = []
        with open("json-files/hate.json", "r") as f:
            data = json.load(f)
            if username in data:
                for thing in data[username]:
                    likeness.append(thing)
            else:
                return "sorry, you were not found in the file"
