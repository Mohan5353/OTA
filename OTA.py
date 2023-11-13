import network
from urequests import get
import os
import json
import machine
from utime import sleep

class ota:
    def __init__(self,ssid="Hello",password="NerveCrackedx")->None:
        print("\r\r\r\r\r\r\r\r\r")
        self.ssid=ssid
        self.password=password
        self.url="https://raw.githubusercontent.com/Mohan5353/OTA/main/firmwall/"
        if 'version.json' in os.listdir():    
            with open('version.json') as f:
                self.current_version = json.load(f)['version']
            print(f"Current device firmware version is '{self.current_version}'")

        else:
            self.current_version = 0
            with open('version.json', 'w') as f:
                json.dump({'version': self.current_version}, f)
        self.connect_wifi()
        self.check_download_install()
        
        
    def connect_wifi(self)->None:
        try:
            wifi=network.WLAN(network.STA_IF)
            wifi.active(True)
            wifi.connect(self.ssid,self.password)
            print("Connecting...",end="")
            while not wifi.isconnected():
                print(".",end="")
                sleep(0.25)
            print('\nYour ip Address is',wifi.ifconfig()[0])
        except:
            pass
    
    def check_version(self)->bool:
        self.latest_version=get(self.url+"version.json").json()
        if self.latest_version["version"]!=self.current_version:
            print(f"New Verson Available {self.latest_version["version"]}")
            return True
        print("Device is Up To Date")
        return False
        
    def fetch_latest_code(self,file)->bool:
        try:
            response=get(self.url+file)
            if response.status_code!=200:
                print("Bad Response, File Name is",file)
                return False
            self.latest_code=response.text
            return True
        except:
            return False
    def update_code(self,file)->None:
        with open("latest.py","w") as fp:
            fp.write(self.latest_code)
        os.rename("latest.py",file)
        
    def Restart(self)->None:
        with open("version.json") as fp:
            json.dump(self.latest_version,fp)
        for i in range(5,0,-1):
            print("Applying Updates in",i,end='\r')
        machine.reset()
    
    def check_download_install(self)->None:
        if self.check_version():
            files=self.latest_version['files']
            for file in files:
                if self.fetch_latest_code(file):
                    self.update_code(file)
            self.Restart()
