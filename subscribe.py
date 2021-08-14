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
    print("      ███████╗███████╗███████╗      ")
    print("      ██╔════╝██╔════╝██╔════╝      ")
    print("█████╗█████╗  ███████╗███████╗█████╗")
    print("╚════╝██╔══╝  ╚════██║╚════██║╚════╝")
    print("      ███████╗███████║███████║      ")
    print("      ╚══════╝╚══════╝╚══════╝      ")
    print()
    print("█████╗█████╗█████╗█████╗█████╗█████╗")
    print("╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝")
    print()
    print()   

    i = 0
    for email in emails:
        comment = email.strip()
        if not comment.startswith("#"):
            i+=1

    print(Fore.GREEN + '> ' + Style.RESET_ALL + f"Loaded {i} emails")
    print()

def error(e, url):
    print(Fore.RED, '>' + Style.RESET_ALL + 'Cloudn\'t subscribe ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + url + 'because ' + e.message)

load()

for email in emails:
    comment = email.strip()
    if comment.startswith("#"):
        continue
    data1.update({"Email": email})
    data2.update({"email": email})
    data3.update({"email": email})
    data4.update({"email": email})
    data5.update({"email": email})
    data6.update({"email": email})
    try:
        try:
            res1 = requests.post('https://www.biblegateway.com/newsletters/subscribe/', allow_redirects=False, data=data1)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.biblegateway.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, "biblegateway.com")
        try:
            res2 = requests.post('https://www.nbc26.com/account/manage-email-preferences', allow_redirects=False, data=data2)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.nbc26.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, "nbc26.com")
        try:
            res3 = requests.post('https://api.ewscloud.com/prod/notifications/v1/wgba/contactlists/subscribe/', allow_redirects=False, data=data3)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'ewscloud.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, 'ewscloud.com')
        try:
            res4 = requests.post('https://activation.healthline.com/api/activate/site', allow_redirects=False, data=data4)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'healthline.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, 'healthline.com')
        try:
            res5 = requests.post('https://api.click2houston.com/sailthru/sailthru/updatelists/new', allow_redirects=False, data=data5)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'click2houston.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, 'click2houston.com')
        try:
            res6 = requests.post('https://www.cbsnews.com/newsletters/xhr/signup', allow_redirects=False, data=data6)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'cbsnews.com')
            time.sleep(0.2)
        except Exception as e:
            error(e, 'cbsnews.com')
    except KeyboardInterrupt:
        exit()