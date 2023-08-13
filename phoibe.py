# imports
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import json
from functions import settings
from functions import time as fTime
from functions import filesay
from functions import feelings
from functions import fun
from functions import internal
from functions import internalFunctions
from functions import moderation
from functions import rules
from functions import translation
from functions import voting
from functions import wheelie
from functions import random


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
browser.find_element(By.CLASS_NAME, 'input-username').send_keys(settings.core.username)
browser.find_element(By.CLASS_NAME, 'input-username.mt-1').send_keys(settings.core.password)
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


# reading and stripping down the messages so that they can be proccesses by the bot
def read_messages():
    raw_text = str(browser.find_elements(By.XPATH, '//*[@class="log-container may-transform"]')[-1].text)
    return raw_text


def send_message(message):
    browser.find_element(By.XPATH, '//*[@id="app"]/div[23]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/textarea').send_keys(message)
    browser.find_element(By.XPATH, '//*[@id="app"]/div[23]/div[1]/div[2]/div[8]/div[3]/div[1]/div[5]/div[2]/div/div/div[4]').click()



userBuffer = ""
mesBuffer = ""
send_message(random.entrances.entrance())
while True:
    try:

        raw = read_messages()
        raw = raw.split("\n")
        if len(raw) == 3:
            raw.pop(1)
        try:
            username = raw[0]
            message = raw[1]
        except IndexError:
            message = raw[0]
            username = userBuffer
            pass
        if username == "":
            username = userBuffer
        if username != "":
            userBuffer = username
        if message != mesBuffer:
            if settings.miscSettings.logchat is True:
                internalFunctions.logs.writeToLogs(message, username)
            print("[" + username + "]")
            print(message)
            mesBuffer = message

        # blacklist
        if settings.moderation.useBlacklist is True:
            checked = moderation.blacklist.check(username)
            if checked is True:
                message = ""
                internalFunctions.logs.writeToLogs("WARN - " + username + " tried to use a command")
        # commands

        # filesay
        if ".filesay" in message:
            if username in settings.core.trustedUsers:
                command, url = message.split(" ")
                contents = filesay.filesay.filesay(url)
                for thing in contents:
                    time.sleep(3)
                    send_message(thing)
            else:
                send_message("filesay was disabled")
                internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # timezones
        if ".timez" in message:
            if settings.funcSettings.useTimez is True:
                com, tz = message.split(" ")
                send_message(fTime.time.timez(tz))
            else:
                send_message("timez was disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # wheelie
        if ".wheelie" in message:
            if settings.funcSettings.useWheelie is True:
                com, com2 = message.split(" ")
                resp = wheelie.wheelie.wheelie(com2)
                for thing in resp:
                    send_message(thing)
                    time.sleep(3)
            else:
                send_message("wheelie has been disabled (this is stupid, turn it back on)")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # fight
        if ".fight" in message:
            if settings.funcSettings.useFight is True:
                com, user1, user2 = message.split(" ")
                send_message(fun.fight.fight(user1, user2))
            else:
                send_message("fight has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # custom messages
        if settings.core.name in message:
            if settings.funcSettings.useCMessages is True:
                send_message(fun.messages.custom(username))
        # urbandict
        if ".urbandict" in message:
            if settings.funcSettings.useUrbandict is True:
                com, term = message.split(" ", maxsplit=1)
                send_message(fun.urbandict.getDef(term))
            else:
                send_message("urbandict has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # rules
        if ".rules" in message:
            if settings.funcSettings.useRules is True:
                rules = rules.rules.read()
                for thing in rules:
                    send_message(rules)
                    time.sleep(3)
            else:
                send_message("rules was disabled (please change this)")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # specific rule
        if ".srule" in message:
            if settings.funcSettings.useSRule is True:
                com, rule = message.split(" ")
                send_message(rules.rules.srule(rule))
            else:
                send_message("srule has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # translation
        if ".translate" in message:
            if settings.funcSettings.useTranslations is True:
                goodies = message.split(" ", maxsplit=1)
                updatedGoodies = goodies[1].rsplit(" ", 1)
                send_message(translation.deepl.translate(updatedGoodies[0], updatedGoodies[1]))
            else:
                send_message("management has disabled translation")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # voice
        if ".voice-vote" in message:
            if settings.funcSettings.useVote is True:
                if username in moderation.minimods.mMods():
                    com, vote = message.split(" ")
                    voting.voice.vote(username, vote),
                    send_message(username + " has voted")
                else:
                    send_message("you are not allowed to use this command")
            else:
                send_message("voting has been disabled")    
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # clear voice
        if ".voice-clear" in message:
            if settings.funcSettings.useVote is True:
                if username in settings.core.trustedUSers:
                    voting.voice.clear()
                else:
                    send_message("you are not allowed to use this command")
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # counting voice votes
        if ".voice-count" in message:
            if settings.funcSettings.useVote is True:
                if username in settings.core.trustedUsers:
                    votes = voting.voice.read()
                    yays = votes[0]
                    nays = votes[1]
                    send_message("yays: " + yays + " | " + "nays: " + nays)
                else:
                    send_message("you are not allowed to use this command")
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # canidate voting
        if ".multi-vote" in message:
            if settings.funcSettings.useVote is True:
                if username in moderation.minimods.mMods():
                    com, candidate = message.split(" ")
                    voting.multi.castVote(username, candidate)
                    send_message("you have voted")
                else:
                    send_message("you are not allowed to vote")
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # issue
        if ".issue" in message:
            if settings.funcSettings.useVote is True:
                send_message(voting.multi.issue)
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # multi results
        if ".multi-results" in message:
            if settings.funcSettings.useVote is True:
                send_message(voting.multi.results())
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # multi ballot
        if ".multi-ballot" in message:
            if settings.funcSettings.useVote is True:
                ballot = voting.multi.ballot()
                for candidate in ballot:
                    send_message(candidate)
                    time.sleep(3)
            else:
                send_message("voting has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # random stuff
        if ".drink" in message:
            if settings.funcSettings.useDrink is True:
                try:
                    com, user = message.split(" ")
                except ValueError:
                    user = username
                send_message(random.drink.drink(user))
            else:
                send_message("drinking has been disabled, how sad")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # joke
        if ".joke" in message:
            if settings.funcSettings.useJokes is True:
                send_message(random.joke.joke())
            else:
                send_message("joking is not allowed in this tyrannical room")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # insult
        if ".insult" in message:
            if settings.funcSettings.useInsults is True:
                send_message(random.insults.insult())
            else:
                send_message("ok, this one kinda makes sense, but it's still disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
        # cuss
        if ".cuss" in message:
            if settings.funcSettings.useCuss is True:
                send_message(random.cuss.cuss())
            else:
                send_message("this command has been disabled")
            internalFunctions.logs.writeToLogs("INFO - " + username + " used a command")
    except KeyboardInterrupt():
        print("interrupt recieved")
