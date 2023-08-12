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








# get username and shit from the json file
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
send_message("This is a development build of phoibe")
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
    except KeyboardInterrupt():
        print("interrupt recieved")
