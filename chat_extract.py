from datetime import datetime
import re
import pandas as pd
from time import sleep

lines = []

with open("chat.log", 'r', encoding='utf-8') as f:
    lines = f.read().split('\n\n\n')

lines = lines[:-1]

for idx, msg in enumerate(lines):    
    time_logged = msg.split()[0].strip()

    time_logged = datetime.strptime(time_logged, '%Y-%m-%d_%H:%M:%S')

    username_message = msg.split('—')[1:]
    username_message = '—'.join(username_message).strip()
    
    try:
        username, channel, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', username_message).groups()
        #print(f"Channel: {channel} \nUsername: {username} \nMessage: {message}")
        print(f"Message: {message}")
    except: print("-----")

    print("\n")
    