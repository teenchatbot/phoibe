import json


class likes:
    def get_like(like, username):
        success = False
        bannedChars = ["'}", "']" "."]
        like = like.strip(bannedChars)
        with open("json-files/likes.json", "r") as f:
            data = json.load(f)
            if username in data:
                data[username].append(like)
                success = True
                return success
            else:
                data[username] = [like]
                success = True
                return success
        with open("json-files/likes.json", "w") as f:
            json.dump(data, f, indent=4)

    def read_like(username):
        with open("json-files/likes.json", "r") as f:
            data = json.load(f)
            if username in data:
                return data
            else:
                return "sorry, you were not found in the file"


class hates:
    def get_hate(like, username):
        success = False
        bannedChars = ["'}", "']" "."]
        like = like.strip(bannedChars)
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
        with open("json-files/hate.json", "r") as f:
            data = json.load(f)
            if username in data:
                return data
            else:
                return "sorry, you were not found in the file"
