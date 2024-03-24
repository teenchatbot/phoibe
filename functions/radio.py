import requests
import urllib3
import settings


class radio:
    def checkStation():
        http = urllib3.PoolManager()
        try:
            resp = http.request("GET", settings.)

