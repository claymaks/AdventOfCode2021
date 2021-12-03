import os
import sys
import requests
import subprocess
import shutil
import datetime

YEAR = 2021
DAY = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Day: "))

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

response = None
now = datetime.datetime.now()
target = datetime.datetime(YEAR, 12, DAY)
if now > target:
    uri = f"http://adventofcode.com/{YEAR}/day/{DAY}/input"
    response = requests.get(uri, cookies={'session': SESSIONID})

# Create new day folder based on template.
if not os.path.exists(os.path.dirname(f"day{DAY}")):
    print(f"Creating day{DAY} folder")
    if os.path.exists(f"day_template"):
        shutil.copytree(f"day_template", f"day{DAY}")
    else:
        print("No template folder named day_template", file=sys.stderr)
else:
    print(f"day{DAY} folder already exists!", file=sys.stderr)

os.system(f"open -a Terminal {os.path.join(os.getcwd(), f'day{DAY}')}")

# Exit early if we failed to pull data or the data won't be available
if response is None:
    sys.exit(f"Data accessed too early! it's {now}, not {target}.")
elif not response.ok:
    sys.exit(f"Request for input failed! {response}: {response.reason}")
    
    
print("Request for input succeeded!")
with open(f"day{DAY}/input", 'w') as f:
    f.write(response.text)
