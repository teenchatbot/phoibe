from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
<<<<<<< HEAD
import json
=======

>>>>>>> origin/nightly

class backlog:
    def assign(username):
        try:
            if username != "read":
                return "ok, " + username + " has been reported"
        except:
            return "an error has occured"
    def read():
        usernames = open("./syscrit/people/backlog.txt", "r")
        usernames = str(usernames.read())
        usernames = usernames.replace("\n", " ")
        return usernames
class blacklist:
    def check(username):
        blacklist = open("./syscrit/people/blacklist.txt", "r")
        blacklist = str(blacklist.read)
        true_blacklist = blacklist.split("\n")
        if username in true_blacklist:
            return True
        else:
            return False
class minimods:
    def mMods():
        with open("./syscrit/people/minimods.txt") as f:
            lin = f.read()
            lines = lin.split("\n")
            return lines
    def test():
        return "your test has been successful"
class regUsers:
    def check(username):
        with open("./syscrit/people/regusers.txt", "r") as f:
            lin = str(f.read())
            users = lin.split("\n")
            if username in users:
                return True
            else:
                return False
class moderator:
    def get_muted_users():
        with open("syscrit/people/mute.txt", "r") as file:
            lines = file.read()
            lines = lines.split("\n")
            return lines
    def delete_message(browser):
        message = browser.find_elements(By.XPATH, '//*[@class="message-tooltip show-on-hover"]')
        e = browser.find_elements(By.XPATH, '//*[@class="text_wrapper"]')

        if e:
            e = e[-1]
            ActionChains(browser).move_to_element(e).perform()
            ActionChains(browser).move_to_element(message[-1]).perform()

            f = browser.find_elements(By.XPATH, '//*[@class="btn btn--flat btn--icon"]')
            ActionChains(browser).move_to_element(f[-1]).click().perform()
            browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/a/div[2]/div').click()
            time.sleep(1)
<<<<<<< HEAD
    def HornyScore(message):
        hornyscore = 0
        with open("json-files/naughtywords.json", "r") as file:
            data = json.load(file)

        for word in message.split(" "):
            if word in data.keys():
                hornyscore = hornyscore + data[word]

        return hornyscore
=======
>>>>>>> origin/nightly
