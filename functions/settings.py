import json

# the overarching settings file
settingsfile = open("json-files/settings.json", "r")
settingsdata = json.load(settingsfile)


class core:
    username = settingsdata['core']['username']
    password = settingsdata['core']['password']
    entrances = settingsdata['core']['entrances']
    name = settingsdata['core']['name']
    version = settingsdata['core']['version']
class miscSettings:
    logchat = settingsdata['miscInfo']['LogChat']
    trustedUsers = settingsdata['miscInfo']['trustedUser']







settingsfile.close()
