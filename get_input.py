import os
import sys
import requests
import subprocess

YEAR = 2021
DAY = sys.argv[1] if len(sys.argv) > 1 else input("Day: ")

def get_session_id():
    with open('session', 'r') as f:
        return f.readline()


SESSIONID = None
try:
    SESSIONID = get_session_id()
except FileNotFoundError:
    print("AOC2021 SESSION ID not found!")
    SESSIONID = input("Input 'session' from cookie here: ")

    # Store session ID.
    with open('session', 'w') as f:
        f.write(SESSIONID)

    # Add it to .gitignore, making a new one if it doesn't exist.
    with open('.gitignore', 'a+') as f:
        f.write('session\n')
    

uri = f"http://adventofcode.com/{YEAR}/day/{DAY}/input"
response = requests.get(uri, cookies={'session': SESSIONID})

with open(f"day{DAY}/input", 'w') as f:
    f.write(response.text)
