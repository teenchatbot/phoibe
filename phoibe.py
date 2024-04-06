# imports

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# non function, but still important imports
import time
import random
import json
import threading
import socket


# function imports
from functions import settings
from functions import timeFunctions as fTime
from functions import filesay
from functions import feelings
from functions import fun
from functions import internal
from functions import internalFunctions
from functions import moderation
from functions import rules
from functions import tran
from functions import voting
from functions import wheelie
from functions import Frandom
from functions import UCAL
from functions import services

# selenium shit


opts = Options()
opts.add_argument("--headless")
browser = webdriver.Firefox(options=opts)
browser.get("https://y99.in/web/login/")
a = ActionChains(browser)


# find the button to login to an account
access_y99_button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'blue--text.login-instead')))
# click the button found above
access_y99_button.click()

# input the username
browser.find_element(By.CLASS_NAME, 'input-username').send_keys(settings.core.username)
# input the password
browser.find_element(By.CLASS_NAME, 'input-username.mt-1').send_keys(settings.core.password)
# click the button to login
browser.find_element(By.CLASS_NAME, 'mx-0.btn.btn--large.btn--depressed.e4jtrd').click()
print("Logged in")

# get past the staging page

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="welcome-page"]/div/div[3]/button'))).click()
print("past the staging page")

# Firefox options go here

# Get rid of the popup

WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[12]/div/div/div[3]/button[1]'))).click()

print("got rid of the popup")
print("entering the chat")

# lookup the room by room code
searchRoom = WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[9]/div/div[2]/input')))
searchRoom.click()
time.sleep(.1)
searchRoom.send_keys(settings.core.room)

# enter the chatroom with the code from settings.json
chatroom = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[9]/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div[3]/button[1]')))
chatroom.click()
time.sleep(.5)
print("entered the chat")





# reading and stripping down the messages so that they can be proccesses by the bot
def read_messages():
    time.sleep(.2)
    WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, '//*[@class="log-container may-transform"]')))
    LastMessage = browser.find_elements(By.XPATH, '//*[@class="log-container may-transform"]')[-1]
    try:
        message_text = LastMessage.find_element(By.CLASS_NAME, 'text').text
    except Exception:
        message_text = ""
    username_text = LastMessage.find_element(By.CLASS_NAME, 'username').text
    return username_text, message_text




def send_message(message):
    time.sleep(.2)
    global userBuffer
    userBuffer = settings.core.username
    text_area = browser.find_element(By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/textarea')
    text_area.click()
    text_area.send_keys(message)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[26]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/div[4]').click()

# Websocket stuff
HOST = '127.0.0.1'
PORT = 8080

def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            s.send(data.encode('utf-8'))
        except Exception:
            pass
def data_gen():
    while True:
        data_to_send = acquire_data()
        send_data(data_to_send)
        time.sleep(1) # this is REQUIRED, I have no idea why, it just is
def acquire_data():
    data = data_holder[0]
    return data

data_holder = ["Phoibe:connection established"]

data_thread = threading.Thread(target=data_gen())
data_thread.daemon = True
data_thread.start()



userBuffer = settings.core.username
mesBuffer = ""
time.sleep(.3)
send_message(Frandom.entrances.entrance())
while True:
    try:
        username, message = read_messages()
        if message == "":
            message = "(No Message)"
        if username == "":
            username = userBuffer
        if username != "":
            userBuffer = username
        if message != mesBuffer:
            if settings.miscSettings.logchat is True:
                try:
                    internalFunctions.logs.writeToLogs(message, username)
                except:
                    print("")
            mesBuffer = message
            print("[" + username + "]")
            print(message)
            formattedMessage = username + ":" + message # use this format so that the client (read GUI) can easily digest the data in a better way
            data_holder[0] = formattedMessage
# commands

# good morning and good night
        if ".gm" in message:
            send_message("good morning sleepyhead")
        if ".gn" in message:
            send_message("good night my little pumpkin boo")

# feelings
        if ".melike" in message:
            if settings.funcSettings.useGetLike is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.GetLike) is True:
                        try:
                            command, like = message.split(" ", maxsplit=1)
                            feelings.likes.get_like(like, username)
                            send_message("it's offical" + " " + username + " likes " + like)
                        except Exception as e:
                            send_message("An unknown error has occured here is your error: " + str(e))
                    else:
                        send_message("your UCAL level is not high enough")
                else:
                    try:
                        command, like = message.split(" ", maxsplit=1)
                        feelings.likes.get_like(like, username)
                        send_message("it's offical" + " " + username + " likes " + like)
                    except Exception as e:
                        send_message("An unknown error has occured here is your error: " + str(e))
            else:
                send_message("liking has been disabled")
# reading the likes
        if ".whatlike" in message:
            if settings.funcSettings.useGetLike is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.ReadLike) is True:
                        send_message(str(feelings.likes.read_like(username)))
                    else:
                        send_message("your UCAL level is not high enough")
                else:
                    send_message(feelings.likes.read_like(username))
            else:
                send_message("liking has been disabled")
# hates
        if ".mehate" in message:
            if settings.funcSettings.useGetHate is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.GetHate) is True:
                        try:
                            command, like = message.split(" ", maxsplit=1)
                            feelings.hates.get_hate(like, username)
                            send_message("It's offical, " + username + " hates " + like)
                        except Exception as e:
                            send_message("An unknown error has occured here is your error: " + str(e))
                    else:
                        send_message("your UCAL level is not high enough")
                else:
                    try:
                        command, like = message.split(" ", maxsplit=1)
                        feelings.hates.get_hate(like, username)
                        send_message("It's offical, " + username + " hates " + like)
                    except Exception as e:
                        send_message("An unknown error has occured here is your error: " + str(e))
            else:
                send_message("hating has been disabled")
# reading the likes
        if ".whathate" in message:
            if settings.funcSettings.useGetHate is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.ReadHate) is True:
                        send_message(str(feelings.hates.read_like(username)))
                    else:
                        send_message("your UCAL level is not high enough")
                else:
                    send_message(str(feelings.hates.read_like(username)))
            else:
                send_message("hating has been disabled")
# filesay
        if ".filesay" in message:
            if settings.funcSettings.useFilsay is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Filsay) is True:
                        command, url = message.split(" ")
                        contents = filesay.filesay.filesay(url)
                        for thing in contents:
                            time.sleep(3)
                            send_message(thing)
                        com, tz = message.split(" ")
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    try:
                        send_message(fTime.time.timez(tz))
                    except:
                        send_message("you most likely misspelled the timezone")
            else:
                send_message("this command has been disabled")
# timezones
        if ".timez" in message:
            if settings.funcSettings.useTimez is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Fight) is True:
                        com, tz = message.split(" ")
                        try:
                            send_message(fTime.time.timez(tz))
                        except:
                            send_message("you most likely misspelled the timezone")
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    com, tz = message.split(" ")
                    try:
                        send_message(fTime.time.timez(tz))
                    except:
                        send_message("you most likely misspelled the timezone")
            else:
                send_message("this command has been disabled")
# wheelie
        if ".wheelie" in message:
            if settings.funcSettings.useWheelie is True:
                try:
                    com, com2 = message.split(" ")
                    resp = wheelie.wheelie.wheelie(com2)
                    for thing in resp:
                        send_message(thing)
                        time.sleep(3)
                except:
                    send_message("an error has occured with your request,  please try again")
            else:
                send_message("wheelie has been disabled (this is stupid, turn it back on)")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# fight
        if ".fight" in message:
            if settings.funcSettings.useFight is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Fight) is True:
                        try:
                            com, user1, user2 = message.split(" ")
                            send_message(fun.fight.fight(user1, user2))
                        except Exception as e:
                            send_message(str(e))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    try:
                        com, user1, user2 = message.split(" ")
                        send_message(fun.fight.fight(user1, user2))
                    except Exception as e:
                        send_message(str(e))
            else:
                send_message("this command has been disabled")
# custom messages
        if settings.core.name in message:
            if settings.funcSettings.useCMessages is True:
                send_message(fun.messages.custom(username))
# urbandict
        if ".urbandict" in message:
            if settings.funcSettings.useUrbandict is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Urbandict) is True:
                        com, term = message.split(" ", maxsplit=1)
                        send_message(fun.urbandict.getDef(term))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    com, term = message.split(" ", maxsplit=1)
                    send_message(fun.urbandict.getdef(term))
            else:
                send_message("this command has been disabled")
# rules
        if ".rules" in message:
            if settings.funcSettings.useRules is True:
                if settings.funcSettings.useUcal is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Rules) is True:
                        rules = rules.rules.readrules()
                        for thing in rules:
                            send_message(thing)
                            time.sleep(3)
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    rules = rules.rules.read()
                    for thing in rules:
                        send_message(thing)
                        time.sleep(3)
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# specific rule
        if ".srule" in message:
            if settings.funcSettings.useSRule is True:
                if settings.funcSettings.useUcal is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.SRule) is True:
                        com, rule = message.split(" ")
                        send_message(rules.rules.srule(rule))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    com, rule = message.split(" ")
                    send_message(rules.rules.srule(rule))
            else:
                send_message("srule has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# translation
        if ".translate" in message:
            if settings.funcSettings.useTranslations is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Translations) is True:
                        goodies = message.split(" ", maxsplit=1)
                        updatedGoodies = goodies[1].rsplit(" ", 1)
                        send_message(tran.tran.translate(updatedGoodies[0], updatedGoodies[1]))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    goodies = message.split(" ", maxsplit=1)
                    updatedGoodies = goodies[1].rsplit(" ", 1)
                    send_message(tran.tran.translate(updatedGoodies[0], updatedGoodies[1]))
            else:
                send_message("this command has been disabled")
# voice
        if ".voice-vote" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        com, vote = message.split(" ")
                        voting.voice.vote(username, vote)
                        send_message("done")
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    com, vote = message.split(" ")
                    voting.voice.vote(username, vote)
                    send_message("done")
            else:
                send_message("this command has been disabled")
# clear voice
        if ".voice-clear" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, 80) is True:
                        voting.voice.clear()
                        send_message("done")
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    voting.voice.clear()
                    send_message("done")
            else:
                send_message("this command has been disabled")
# counting voice votes
        if ".voice-count" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        votes = voting.voice.read()
                        yays = votes[0]
                        nays = votes[1]
                        send_message("yays: " + yays + " | " + "nayes: " + nays)
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    votes = voting.voice.read()
                    yays = votes[0]
                    nays = votes[1]
                    send_message("yays: " + yays + " | " + "nayes: " + nays)
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# canidate voting
        if ".multi-vote" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        try:
                            com, candidate = message.split(" ")
                            voting.multi.castVote(username, candidate)
                            send_message("you have voted")
                        except Exception as e:
                            send_message(str(e))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    try:
                        com, candidate = message.split(" ")
                        voting.multi.castVote(username, candidate)
                        send_message("you have voted")
                    except Exception as e:
                        send_message(str(e))
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# issue
        if ".issue" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        send_message(voting.multi.issue())
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message(voting.multi.issue())
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# multi results
        if ".multi-results" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        results = voting.multi.results()
                        send_message(str(results))

                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message(voting.multi.results())
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# multi ballot
        if ".multi-ballot" in message:
            if settings.funcSettings.useVote is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Vote) is True:
                        ballot = voting.multi.ballot()
                        for candidate in ballot:
                            send_message(candidate)
                            time.sleep(3)
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    ballot = voting.multi.ballot()
                    for candidate in ballot:
                        send_message(candidate)
                        time.sleep(3)
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# random stuff
        if ".drink" in message:
            if settings.funcSettings.useDrink is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Drink) is True:
                        try:
                            com, user = message.split(" ")
                        except ValueError:
                            user = username
                        send_message(Frandom.drink.drink(user))
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    try:
                        com, user = message.split(" ")
                    except ValueError:
                        user = username
                    send_message(Frandom.drink.drink(user))
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# joke
        if ".joke" in message:
            if settings.funcSettings.useJokes is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Jokes) is True:
                        send_message(Frandom.joke.joke())
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message(Frandom.joke.joke())
            else:
                send_message("joking is not allowed in this tyrannical room")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# insult
        if ".insult" in message:
            if settings.funcSettings.useInsults is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Insults) is True:
                        send_message(Frandom.insults.insult())
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message(Frandom.insults.insult())
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# cuss
        if ".cuss" in message:
            if settings.funcSettings.useCuss is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Cuss) is True:
                        send_message(Frandom.cuss.cuss())
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message(Frandom.cuss.cuss())
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
# vend
        if ".vend" in message:
            if settings.funcSettings.useVend is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.vend) is True:
                        try:
                            com, user = message.split(" ")
                        except ValueError:
                            user = username
                        send_message(Frandom.vend.vend(user))
                    else:
                        send_message("your ucal level is not high enough to use this command")
                else:
                    try:
                        com, user = message.split(" ")
                    except ValueError:
                        user = username
                    send_message(Frandom.vend.vend(user))
            else:
                send_message("this room has vend disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")

# wew
        if ".wew" in message:
            if settings.funcSettings.useWew is True:
                send_message("what is that?")
            else:
                send_message("it was disabled, how sad")
# ping
        if ".ping" in message:
            if settings.funcSettings.usePing is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.Ping) is True:
                        send_message("pong")
                    else:
                        send_message("you do not have a high enough UCAL level")
                else:
                    send_message("pong")
            else:
                send_message("ping has been turned off")
# raise level
        if ".raiseLevel" in message:
            if settings.funcSettings.useRaiseLevel is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.raiseLevel) is True:
                        com, target, level = message.split(" ")
                        UCAL.ucal.raiseLevel(target, level)
                        send_message(target + "'s level has been raised by " + level)
                    else:
                        send_message("your ucal level is not high enough")
                else:
                    send_message("UCAL is not used in this room")
            else:
                send_message("UCAL is not used in this room, you must like killing puppies")
# alert
        if ".alert" in message:
            if settings.funcSettings.useAlert is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.alert) is True:
                        names = services.services.alert()
                        names = names.split("\n")
                        for name in names:
                            send_message(name)
                            time.sleep(3)
                    else:
                        send_message("your UCAL level is not high enough to use this command")
                else:
                    names = services.services.alert()
                    names = names.split("\n")
                    for name in names:
                        send_message(name)
                        time.sleep(3)
            else:
                send_message("alert has been disabled")
            internalFunctions.logs.writeToLogs("INFO - [" + username + "] used a command")
# roll
        if ".roll" in message:
            if settings.funcSettings.useDice is True:
                if settings.funcSettings.useUCAL is True:
                    if UCAL.ucal.check(username, settings.ucalLevels.dice) is True:
                        try:
                            com, side = message.split(" ")
                            side = int(side)
                        except:
                            side = 6
                        send_message(Frandom.dice.roll(side))
                    else:
                        send_message("your UCAL level is not high enough to use this command")
                else:
                    try:
                        com, side = message.split(" ")
                        side = int(side)
                    except IndexError:
                        side = 6
                    send_message(Frandom.dice.roll(side))
            else:
                send_message("this command has been disabled")
# URL translater
        if settings.funcSettings.translateURLs:
            if services.urls.checkIfURL(message):
                try:
                    url = services.urls.getURL(message)
                    send_message(services.urls.findURL(url))
                except Exception as e:
                    send_message(str(e))
        # have ucal add all new users
        UCAL.ucal.add(username)
        if settings.funcSettings.useDeletion is True:
            if moderation.moderator.HornyScore(message) >= 100:
                try:
                    moderation.moderator.delete_message(browser)
                    send_message("/notice your message have been removed with a HornyScore of " + str(moderation.moderator.HornyScore(message)))
                except Exception as e:
                    send_message("an error has occurred with deleting your message, your error is " + str(e))
            for thing in settings.moderation.triggers:
                if thing in message:
                    try:
                        moderation.moderator.delete_message(browser)
                        send_message("/notice watch what you say")
                    except Exception as e:
                        send_message("an error has occurred with deleting your message, your error is " + str(e))
    except KeyboardInterrupt():
        print("interrupt recieved")

