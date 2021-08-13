import requests
import time
from colorama import Fore, Style, init
from reqdata import *

init()
f = open("emails.txt", "r")
emails = f.read().splitlines()

def load():
    print()
    print()
    print("█████╗█████╗█████╗█████╗█████╗█████╗")
    print("╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝")
    print()
    print()
    print()
    print("      ███████╗███████╗███████╗      ")
    print("      ██╔════╝██╔════╝██╔════╝      ")
    print("█████╗█████╗  ███████╗███████╗█████╗")
    print("╚════╝██╔══╝  ╚════██║╚════██║╚════╝")
    print("      ███████╗███████║███████║      ")
    print("      ╚══════╝╚══════╝╚══════╝      ")
    print()
    print()
    print()
    print("█████╗█████╗█████╗█████╗█████╗█████╗")
    print("╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝")
    print()
    print()   

    i = 0
    for email in emails:
        i+=1

    print(Fore.GREEN + '> ' + Style.RESET_ALL + f"Loaded {i} emails")
    print()

def error(e, url):
    print(Fore.RED, '>' + Style.RESET_ALL + 'Cloudn\'t subscribe ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + url + 'because ' + e.message)

load()

for email in emails:
    data1.update({"Email": email})
    data2.update({"email": email})
    data3.update({"email": email})
    try:
        try:
            res1 = requests.post('https://www.biblegateway.com/newsletters/subscribe/', allow_redirects=False, data=data1)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.biblegateway.com')
            time.sleep(0.3)
        except Exception as e:
            error(e, "biblegateway.com")

        try:
            res2 = requests.post('https://www.nbc26.com/account/manage-email-preferences', allow_redirects=False, data=data2)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.nbc26.com')
            time.sleep(0.3)
        except Exception as e:
            error(e, "nbc26.com")

        try:
            res3 = requests.post('https://api.ewscloud.com/prod/notifications/v1/wgba/contactlists/subscribe/', allow_redirects=False, data=data3)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'api.ewscloud.com')
            time.sleep(0.3)
        except Exception as e:
            error(e, 'ewscloud.com')
    except KeyboardInterrupt:
        exit()