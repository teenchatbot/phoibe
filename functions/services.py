# this outlines stuff like alert
from bs4 import BeautifulSoup
import requests


class services:
    def alert():
        with open("syscrit/people/alert.txt", "r") as file:
            lines = file.read()
        return lines


class urls:
    def checkIfURL(message):
        if 'https://' in message:
            return True
        if 'http://' in message:
            return True
        else:
            return False

    def getURL(message):
        spaces = message.split(" ")
        for x in spaces:
            if 'https://' or 'http://':
                return x

    def findURL(url):
        reqs = requests.get(url)
        try:
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for title in soup.find_all('title'):
                return title.get_text()
        except:
            return "an error occured when trying to retrieve the webpage"
