import os
from zipfile import ZipFile
import json
import shutil


url = "https://github.com/teenchatbot/phoibe/releases/download/v2.0.1/phoibe-mucho.zip"


# Download the file
print("Downloading...")
os.system("curl -L " + url + " -o latest.zip")
print("download complete...")
print("extracting the zip file")
# the .zip file is now done

# extract the zip
with ZipFile("./latest.zip") as zObject:
    zObject.extractall("./")
# the .zip has been extracted

# compare differences

# check the length of the settings file to the one that's in the new release
# old settings file
with open("./../json-files/settings.json", "r") as oldSets:
    lines = oldSets.readlines()
    totalLines = len(lines)
# new settings file
with open("./phoibe-mucho/json-files/settings.json", "r") as newSets:
    lines = newSets.readlines()
    totalLines2 = len(lines)
if totalLines != totalLines2:
    print("looks like there were some changes to the settings files")

# to preserve the users already saved settings, loop through their old settings.json and check to see if the same setting in the new one is the same,
# if it is not, then rewrite their old setting to their new one
newSetsFile = open("./phoibe-mucho/json-files/settings.json")
with open("./../json-files/settings.json", "r") as settingsFile:
    data = json.load(settingsFile)
    newdata = json.load(newSetsFile)
    # find and change non default data
    for thing in data:
        for thingie in data[thing]:
            try:
                if newdata[thing][thingie] != data[thing][thingie]:
                    print("Delta match found")
                    print(str(newdata[thing][thingie]) + " is not the same as " + str(data[thing][thingie]))
                    with open("./phoibe-much/json-files/settings.json", "w") as change:
                        changeme = json.load(change)
                        newdata[thing][thingie] = data[thing][thingie]
                        print("data preserved")
                        json.dump(newdata, newSetsFile, indent=4)
            except Exception as e:
                print("new setting found")
newSetsFile.close()


# delete the old files


# ask for user input to close
input("press enter to finish")
