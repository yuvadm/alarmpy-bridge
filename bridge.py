import requests
# import boto

from time import sleep

class AlarmpyBridge():
    URL = "https://www.oref.org.il/WarningMessages/alert/alerts.json"

    HEADERS = {
        "Referer": "https://www.oref.org.il/11226-he/pakar.aspx",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }

    def __init__(self):
        self.sess = requests.Session(headers=self.HEADERS)
        self.last = None

    def loop(self):
        print("Starting Alarmpy Bridge loop...")
        while True:
            try:
                self.fetch()
            except Exception as e:
                print(e)
                pass
            finally:
                sleep(0.5)
    
    def fetch(self):
        res = self.sess.get(self.URL).content
        print(f"Got {res}")
        if res != self.last:
            self.update(res)
        self.last = res
    
    def update(self, res):
        print(f"Updating {res}")

if __name__== "__main__":
    ab = AlarmpyBridge()
    ab.loop()