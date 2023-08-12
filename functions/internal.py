# imports may be needed, maybe not
import json
import requests
import base64
import datetime
import hashlib


class getVersion:
    # this is for checking the versions and stuff

    def getVersion():
        file = open("json-files/settings.json", "r")
        data = json.load(file)
        content = data['core']['version']
        print(content)
        ver, version, codename = content.split(" ")
        return version


class checkVersion:
    def checkVersion():
        installedVersion = getVersion.getVersion()
        url = 'https://api.github.com/repos/teenchatbot/botversion/contents/version.txt'
        req = requests.get(url)
        if req.status_code == requests.codes.ok:
            req = req.json()
            content = base64.b64decode(req['content'])
            content = content.decode()
            ver, version, codename = content.split(" ")
            print(version + " " + installedVersion)
            if version == installedVersion:
                return "your version is up to date"
            else:
                return "your version (" + version + ") " + "needs to be updated"
        else:
            print("content not found")

class hashes:
    def check():
        try:
            now = datetime.datetime.now()
            now = now.strftime('%Y-%m-%d')
            file = './logs/' + now + '.log'
            hashpath = "./hashes/" + now + ".hash"
            try:
                hashpath = open(hashpath, "r")
            except:
                hashpath = "woogly"
                return "there was a rare error that occured"
            hashpath = hashpath.read(128)
            file = open(file, "rb")
            file = file.read()
            m = hashlib.sha3_512(file).hexdigest()
            if hashpath != str(m):
                return "the log files were not validated correctly"
        except:
            return "something has happened"
    def hashfile(file, hashpath):
        file = open(file, "rb")
        file = file.read()
        m = hashlib.sha3_512(file).hexdigest()
        with open(hashpath, "w+") as f:
            f.write(str(m))
