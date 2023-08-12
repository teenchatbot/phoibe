import requests


class filesay:
    def filesay(url):
        contents = requests.get(url).text.split("\n")
        return contents
