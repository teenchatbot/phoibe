# imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
import time
import datetime
from datetime import date
import pytz
import random
import socket
import urllib3
import urllib3.exceptions
import threading
import deepl
# from newsapi import NewsApiClient
import re
import requests
import smtplib
import json
# from win32gui import GetWindowText, GetForegroundWindow
from translate import Translator
import langid
import os
import subprocess
import hashlib
import base64

# get username and shit from the json file

settingsfile = open("json-files/settings.json", "r")
settingsdata = json.load(settingsfile)

username = settingsdata['login']['username']
password = settingsdata['login']['password']

entrances = settingsdata['entrances']['entrances']


def logchat():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    logchat = settingsdata['OtherInfo']['LogChat']
    settingsfile.close()
    return logchat


def trustedUser():
    settingsfile = open("json-files/settings.json")
    settingsdata = json.load(settingsfile)
    trustedUsers = settingsdata['OtherInfo']['trustedUser']
    settingsfile.close()
    return trustedUsers


def get_version():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    version = settingsdata['systemsettings']['version']
    settingsfile.close()
    checkVersion()
    return version


def whatsnew():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    whatsnew = settingsdata['systemsettings']['whatsnew']
    settingsfile.close()
    return whatsnew


def get_radio():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    radiolink = settingsdata['radioShit']['radioURL']
    settingsfile.close()
    return radiolink


def get_broadcastlink():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    broadcastlink = settingsdata['radioShit']['broadcastURL']
    settingsfile.close()
    return broadcastlink


def get_name():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    name = settingsdata['OtherInfo']['name']
    settingsfile.close()
    return name


def get_deeplkey():
    settingsfile = open("json-files/settings.json", "r")
    settingsdata = json.load(settingsfile)
    deeplkey = settingsdata['OtherInfo']['DeeplKey']
    settingsfile.close()
    return deeplkey
# random stuff


def get_jokes():
    file = open("json-files/random.json", "r")
    data = json.load(file)
    jokes = data['jokes']
    joke = random.choice(jokes)
    return joke


def get_drink():
    file = open("json-files/random.json", "r")
    data = json.load(file)
    drinks = data['drinks']
    drink = random.choice(drinks)
    return drink


def get_cuss_word():
    file = open("json-files/random.json", "r")
    data = json.load(file)
    words = data['cuss_words']
    word = random.choice(words)
    return word


def get_insults():
    file = open("json-files/random.json", "r")
    data = json.load(file)
    insults = data['insults']
    insult = random.choice(insults)
    return insult


# selinum shit


opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
browser.get("https://y99.in/web/login/")
a = ActionChains(browser)


# get into y99
time.sleep(5)
# access y99
browser.find_element(By.CLASS_NAME, 'blue--text.login-instead').click()
# user and password
browser.find_element(By.CLASS_NAME, 'input-username').send_keys(username)
browser.find_element(By.CLASS_NAME, 'input-username.mt-1').send_keys(password)
browser.find_element(By.CLASS_NAME, 'mx-0.btn.btn--large.btn--depressed.e4jtrd').click()
print("Logged in")
# get past staging page
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="welcome-page"]/div/div[3]/button').click()
print("past the staging page")
# get rid of popup
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="app"]/div[9]/div/div/div[3]/button[1]').click()
print("got rid of popup")
time.sleep(3)
# hop into deep's chat
print("entering the chat")
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="app"]/div[23]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]').click()
print("entered the chat")


def getVersion():
    file = open("json-files/settings.json", "r")
    data = json.load(file)
    version = data['systemsettings']['version']
    ver, version, codename = version.split(" ")
    return version


def saveVersion():
    version = getVersion()
    with open("version.txt", "r+") as f:
        f.write(version)


def checkVersion():
    installedVersion = getVersion()
    url = 'https://api.github.com/repos/teenchatbot/botversion/contents/version.txt'
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = base64.b64decode(req['content'])
        content = content.decode()
        ver, version, codename = content.split(" ")
        print(version)
        print(installedVersion)
        if version == installedVersion:
            send_message("your version is up to date")
        else:
            send_message("you need to update to " + version + ", " + "your version is " + installedVersion)
    else:
        print("content not found")


# reading and stripping down the messages so that they can be proccesses by the bot
def read_messages():
    raw_text = str(browser.find_elements(By.XPATH, '//*[@class="log-container may-transform"]')[-1].text)
    return raw_text
# timer


def timer(h, m, s, user):
    finished = False
    total_seconds = h * 3600 + m * 60 + s
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        time.sleep(1)
        total_seconds -= 1
    send_message("/runban " + user)
# sending messages


def send_message(message):
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[23]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/textarea').send_keys(message)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[23]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/div[4]').click()


def err(errcode):
    writeToLogs("ERROR - " + users + " " + errcode)
    send_message(errcode)


saveVersion()
checkVersion()
send_message(random.choice(entrances))
# filesay


def filesay():
    try:
        useless, url = str3.split(" ", maxsplit=1)
    except:
        pass

    contents = requests.get(url).text.split("\n")
    for shit in contents:
        send_message(shit)
        time.sleep(3)
# time


def read_time():
    now = datetime.datetime.now()
    now = now.strftime("%H:%M:%S")
    proper_time = str("The time in UTC 6 is " + str(now))
    send_message(str(proper_time))
# date


def read_date():
    print("date command recognized")
    send_message(str(date.today()))
# vaduz


def get_vaduz_time():
    print("vaduz command recogized")
    utc_utc_vaduz = datetime.datetime.now(pytz.timezone('Europe/Vaduz'))
    vaduzTime = utc_utc_vaduz.strftime('%d/%m/%Y %H:%M:%S %Z %z')
    send_message(str(vaduzTime))
# timezones


def timez():
    writeToLogs("INFO - [" + users + " used the timez command]")
    goodies = str3.split(" ")
    try:
        timezone = goodies[1]
        timezones = datetime.datetime.now(pytz.timezone(timezone))
        timezonetime = timezones.strftime('%d/%m/%Y %H:%M:%S %Z %z')
        send_message(str(timezonetime))
    except Exception as e:
        writeToLogs("ERROR - [" + users + " caused an error")
        send_message(users + " you caused this error " + str(e))


# station
def get_station():
    print("station command recognized")
    http = urllib3.PoolManager()
    try:
        resp = http.request("GET", get_broadcastlink())
        send_message("The station is broadcasting")
    except:
        send_message("the station is not broadcasting")


# UCAL


# like


def get_like():
    bannedChars = ["['", "']", "{'", "'}", "."]
    try:
        goodies, thingTheyLike = str3.split(" ", maxsplit=1)
        thingTheyLike.strip(bannedChars)
    except:
        pass
    with open("json-files/likes.json", 'r') as f:
        data = json.load(f)
        if users in data:
            data[users].append(thingTheyLike)
            send_message("it's offical, " + users + " likes " + thingTheyLike)
        else:
            data[users] = [thingTheyLike]
            send_message("It's offical, " + users + " likes " + thingTheyLike)
    with open("json-files/likes.json", 'w') as f:
        json.dump(data, f, indent=4)
# hate


def get_hate():
    bannedChars = ["[", "]", "{", "}", "."]
    try:
        goodies, thingTheyLike = str3.split(" ", maxsplit=1)
        thingTheyLike.strip(bannedChars)
    except:
        pass
    else:
        with open("json-files/hate.json", 'r') as f:
            data = json.load(f)
            if users in data:
                data[users].append(thingTheyLike)
                send_message("it's offical, " + users + " hates " + thingTheyLike)
            else:
                data[users] = [thingTheyLike]
                send_message("It's offical, " + users + " hates " + thingTheyLike)
        with open("json-files/hate.json", 'w') as f:
            json.dump(data, f, indent=4)
# read the likes


def read_likes():
    with open("json-files/likes.json", 'r') as f:
        data = json.load(f)
        if users in data:
            send_message(users + " likes " + str(data[users]))
        else:
            send_message("sorry, you were not found in the file")
# read the hates


def read_hate():
    with open("json-files/hate.json", 'r') as f:
        data = json.load(f)
        if users in data:
            send_message(users + " hates " + str(data[users]))
        else:
            send_message("sorry, you were not found in the file")
# backlog


def assign_backlog():
    goodies = str3.split(".")
    goodies = goodies[1].split(" ")
    try:
        if goodies[1] != "read":
            send_message("ok " + goodies[1] + " has been reported to the mods")
            with open("./syscrit/people/backlog.txt", "a") as f:
                f.write(f'{goodies[1]}\n')
    except IndexError:
        err("Unexpected IndexError, please see above command")
        send_message("please read usage")
# read the backlog


def read_backlog():
    usernames = open("./syscrit/people/backlog.txt", "r")
    usernames = str(usernames.read())
    usernames = usernames.replace("\n", " ")
    send_message(usernames)
# translate


def get_transtlation():
    auth_key = get_deeplkey()
    goodies = str3.split(" ", maxsplit=1)
    updatedGoodies = goodies[1].rsplit(" ", 1)
    translator = deepl.Translator(auth_key)
    try:
        send_message(str(translator.translate_text(text=updatedGoodies[0], target_lang=updatedGoodies[1]).text))
    except:
        err("Unexpected translation error has occured")
        send_message("please see the usages for proper language formatting")
# auto backlog

# soft blacklist


def check_blacklist():
    blacklists = open("./syscrit/people/blacklist.txt", "r")
    blacklists = str(blacklists.read())
    true_blacklist = blacklists.split("\n")
    return true_blacklist
# urban dictionary


def get_urban_dictionary_definition(term):
    url = f"https://api.urbandictionary.com/v0/define?term={term}"
    try:
        response = requests.get(url)
        data = response.json()
        if "list" in data and len(data["list"]) > 0:
            first_definition = data["list"][0]["definition"]
            return first_definition
        else:
            return "No definition found."
    except:
        err("Unknown error has occured")


def ud():
    goodies = str3.split(" ", maxsplit=1)
    try:
        definition = get_urban_dictionary_definition(goodies[1])
        send_message(str(definition))
    except:
        writeToLogs("ERROR - [" + users + " caused an IndexError]")
        send_message(users + " you have caused an IndexError, please read the usage and try again")
# voting


def vote():
    goodies = str3.split(" ")
    try:
        if goodies[1] == "yay":
            with open("./syscrit/voting/yay.txt", "a") as f:
                f.write(users + "\n")
                send_message(users + " voted for")
        if goodies[1] == "nay":
            with open("./syscrit/voting/nay.txt", "a") as f:
                f.write(users + "\n")
                send_message(users + " voted against")
    except:
        err("Voting error, this user is either not allowed to vote or something else has happened")
# counting votes


def count_votes():
    yay = []
    nay = []
    with open("./syscrit/voting/yay.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            yay.append(line)
    fixedyay = [*set(yay)]
    with open("./syscrit/voting/nay.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            nay.append(line)
    fixednay = [*set(nay)]
    send_message("yay: " + str(len(fixedyay)) + " nay: " + str(len(fixednay)))
# writing to logs


def writeToLogs(message):
    now1 = datetime.datetime.now()
    now = now1.strftime('%Y-%m-%d %H:%M:%S')
    now2 = now1.strftime('%Y-%m-%d')
    file = "./logs/" + now2 + ".log"
    hashpath = "./hashes/" + now2 + ".hash"
    with open(file, "a+") as f:
        f.write(str(now) + " - " + message +"\n")
    hashfile(file, hashpath)

# this is for hashing the files


def hashfile(file, hashpath):
    file = open(file, "rb")
    file = file.read()
    m = hashlib.sha3_512(file).hexdigest()
    with open(hashpath, "w+") as f:
        f.write(str(m))
# check the hash


def check_hash():
    try:
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d')
        file = "./logs/" + now + ".log"
        hashpath = "./hashes/" + now + ".hash"
        try:
            hashpath = open(hashpath, "r")
        except:
            hashpath = "woogly"
            send_message("there was a rare error that occured with log validation")
        hashpath = hashpath.read(128)
        file = open(file, "rb")
        file = file.read()
        m = hashlib.sha3_512(file).hexdigest()
        if hashpath != str(m):
            send_message("THE LOG HAS FAILED ITS VALIDATION CHECK, SOMEONE HAS TAMPERED WITH THE LOG FILE")
            writeToLogs("ERROR ERROR ERROR - logs failed validation check")
    except:
        send_message("something has happened and Reid is too lazy to fix it")


# checking the issues
def check_issue():
    with open("./syscrit/voting/issue.txt", "r") as f:
        line = f.readline()
        send_message(line)
# hard blacklist


def check_Hblacklist():
    blacklists = open("./syscrit/people/hard_blacklist.txt", "r")
    blacklists = str(blacklists.read())
    true_Hblacklist = blacklists.split("\n")
    return true_Hblacklist
# read the rules


def read_rules():
    f = open("rules.txt", "r")
    rules = str(f.read())
    rules = rules.split('\n')
    for rule in rules:
        send_message(rule)


def srule():
    goodies = str3.split(" ")
    f = open("rules.txt", "r")
    gint = 0
    try:
        gint = int(goodies[1])
        line = f.readlines()
        send_message(str(line[gint - 1]))
    except IndexError:
        writeToLogs("ERROR - something went wrong with reading a specific line from a file")
        send_message("are you possibly using the wrong command? This one is for reading a specific rule, not all of them")
# read the mini mods


def read_mMods():
    f = open("./syscrit/people/minimods.txt", "r")
    lin = f.read()
    lines = lin.split('\n')
    return lines
# mini mod test


def mmtest():
    successful = False
    if users in mini_mod:
        send_message("test is successful")
        successful = True
    else:
        send_message("you are not permitted to use this command")
    return successful
# read the registered users


def read_reg_users():
    f = open("./syscrit/people/regusers.txt", "r")
    lin = str(f.read())
    lines = lin.split('\n')
    return lines
# mini mod echo


def echo():
    goodies = str3.split("/")
    try:
        send_message(goodies[1])
    except:
        writeToLogs("ERROR - [" + users + " has caused an IndexError]")
        send_message(users + " you have cause and IndexError, please read usage and try again")
# mods


def get_mods():
    f = open("./syscrit/people/mods.txt")
    lin = f.read()
    return lin
# casting electoral votes


def cast_vote():
    goodies = str3.split(" ")
    try:
        canidate = goodies[1]
    except IndexError:
        writeToLogs("ERROR - Unexpected IndexError")
        send_message("Unexpected IndexError, please try again")
    file = open("json-files/elect.json", "r")
    file2 = open("./syscrit/voting/haselected.txt", "r")
    file2 = file2.read()
    file2 = file2.split('\n')
    data = json.load(file)
    try:
        if users not in file2:
            data['canidates'][canidate] = data['canidates'][canidate] + 1
            with open("json-files/elect.json", "w") as f:
                json.dump(data, f, indent=4)
            with open("./syscrit/voting/haselected.txt", "a") as f:
                f.write(users + "\n")
        else:
            send_message("you have already voted " + users)
        send_message(users + " has voted")
    except Exception as e:
        writeToLogs("ERROR - [" + users + "caused an error]")
        send_message(users + " you have caused this error: " + str(e))

# sort and then send out the values


def sort_results():
    file = open("json-files/elect.json", "r")
    data = json.load(file)
    data = data['canidates']
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    writeToLogs("INFO - the results have been sorted")
    send_message(str(sorted_data))
# ballot


def get_ballot():
    writeToLogs("INFO - [" + users + " requested the ballot]")
    send_message("please vote for these people with canidate instead of their name")
    f = open("./syscrit/voting/ballot.txt")
    f = f.read()
    f = f.split("\n")
    for canidate in f:
        time.sleep(2)
        send_message(canidate)


def wheelie():
    goodies = str3.split(" ")
    manfile = open("json-files/manual.json", "r")
    man = json.load(manfile)

    try:
        command = goodies[1]
    except:
        writeToLogs("ERROR = [" + users + " caused an IndexError]")
        send_message(users + " you have cause and IndexError, please read the usage of this command by doing (.)wheelie wheelie")
    try:
        send_message("Name: " + man[command]['name'])
        time.sleep(2)
        send_message("Description: " + man[command]['description'])
        time.sleep(2)
        send_message("Usage: " + man[command]['usage'])
    except:
        writeToLogs("ERROR - [" + users + " caused an error with the wheelie command")
        send_message("you have caused an error, please try again")
# fight


def fight():
    basescore1 = 500
    basescore2 = 500

    goodies = str3.split(" ")

    try:
        un1 = goodies[1].lower()
        un2 = goodies[2].lower()
    except:
        writeToLogs("ERROR - [" + users + " caused an IndexError]")

    file = open("json-files/values.json", "r")
    data = json.load(file)
    for letter in un1:
        for shit in data['values']:
            if letter == shit:
                basescore1 = basescore1 + data['values'][shit]
    basescore1 = basescore1 * 100
    for letter in un2:
        for shit in data['values']:
            if letter == shit:
                basescore2 = basescore2 + data['values'][shit]
    basescore2 = basescore2 * 100
    if basescore1 > basescore2:
        send_message(un1 + " won this fight")
    if basescore1 < basescore2:
        send_message(un2 + " won this fight")
    if basescore1 == basescore2:
        send_message("It's a tie")
# muting people


def mute():
    messages = []
    file = open("mute.txt", "r")
    lin = file.readline()
    lines = lin.split("\n")
    for linesx in lines:
        if users in lines:
            messages = browser.find_elements(By.XPATH, '//*[@class="message-tooltip show-on-hover"]')
            e = browser.find_elements(By.XPATH, '//*[@class="text_wrapper"]')
            e = e[-1]
            a.move_to_element(e).perform()
            f = browser.find_elements(By.XPATH, '//*[@class="btn btn--flat btn--icon"]')[-1]
            a.move_to_element(f)
            a.click()
            fuckingwork()


def fuckingwork():
    element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='list__tile__title' and text()='Delete Message']")))
# Click on the element
    a.click(element)


def arabic():
    lang = langid.classify(str3)
    translator = Translator(from_lang='ar', to_lang='en')
    if lang[0] == 'ar':
        translated = translator.translate(str3)
        send_message(translated)


def shell():
    command = str3
    command = command.replace(".sh ", "")
    print(command)
    com = subprocess.Popen((command), shell=True, stdout=subprocess.PIPE).stdout
    com = com.read()
    send_message(com.decode())
# custom messages


def custom_messages():
    f = open("json-files/cMessages.json", "r")
    data = json.load(f)
    if users in data['custom_messages']:
        send_message(data['custom_messages'][users])
    else:
        send_message(users + " what?")


