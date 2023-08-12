import requests


class filesay:
    def filesay(url):
        contents = requests.url(url).text.split("\n")
        return contents
