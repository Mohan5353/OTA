# No implemented Code bro
from uos import remove,listdir
files=listdir()
for file in files:
    if file not in {"OTA.py","main.py","config.py","boot.py","version.json"}:
        remove(file)
