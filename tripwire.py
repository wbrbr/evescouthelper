import requests

class Tripwire:
    
    def __init__(self, username, password):
        r = requests.post('https://tripwire.eve-apps.com/login.php', data={'mode':'login', 'password': password, 'username': username, 'remember': 'off'})
        self.cookies = r.cookies
    
    def load_signatures(self):
        r = requests.post('https://tripwire.eve-apps.com/refresh.php', data={'mode':'init', 'systemID': 31000005, 'systemName': 'Thera'}, cookies=self.cookies)
        return r.json()['signatures']