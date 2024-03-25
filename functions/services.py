# this outlines stuff like alert
import collections
from bs4 import BeautifulSoup
import requests
collections.Callable = collections.abc.Callable

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
        try:
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')
            try:
                for title in soup.find_all('title'):
                    return title.get_text()
            except Exception:
                return "an error occured when trying to retrieve the webpage"
        except Exception:
            return "an error occured when trying to retrieve the webpage"
