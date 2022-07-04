import requests
import random
import time
import os

while True:
    os.system('title discord status changer')
    time.sleep(5)
    headers = {'authorization': 'your token here'}
    status = ['status 1', 'status 2']
    pay = {"custom_status":{"text":(random.choice(status))}}
    r = requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=pay)
    print(+1)
    
    #warning using this is risking your discord account and i will not be held responsible this is for educational purposes
