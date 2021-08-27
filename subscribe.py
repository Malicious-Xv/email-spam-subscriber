import requests
from time import sleep
from colorama import Fore, Style, init
from reqdata import *
import re
from os import system, name
init()
f = open("emails.txt", "r")
emails = f.read().splitlines()

def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def login():
    clear()
    sleep(1)
    print("""
    
    █████╗█████╗█████╗█████╗█████╗█████╗
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
    
          ███████╗███████╗███████╗      
          ██╔════╝██╔════╝██╔════╝      
    █████╗█████╗  ███████╗███████╗█████╗
    ╚════╝██╔══╝  ╚════██║╚════██║╚════╝
          ███████╗███████║███████║      
          ╚══════╝╚══════╝╚══════╝      
    
    █████╗█████╗█████╗█████╗█████╗█████╗
    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
    """)
    print()   
    sleep(1)

    global valid_emails_count
    global valid_emails
    valid_emails_count = 0
    valid_emails = []
    for email in emails:
        is_valid = checkEmail(email)
        if is_valid:
            valid_emails_count += 1
            valid_emails.append(email)

    if valid_emails_count > 0:
        print(Fore.GREEN + '> ' + Style.RESET_ALL + f"Found {valid_emails_count} valid emails")
    elif valid_emails_count == 0:
        print(Fore.RED + '> ' + Style.RESET_ALL + f"Found 0 valid emails")
        exit()

    print()

def error(e, url):
    print(Fore.RED, '>' + Style.RESET_ALL + 'Cloudn\'t subscribe ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + url + Style.RESET_ALL + 'because ' + e)

def main(email):
    data1.update({"Email": email})
    data2.update({"email": email})
    data3.update({"email": email})
    data4.update({"email": email})
    data5.update({"email": email})
    data6.update({"email": email})
    try:
        try:
            res1 = requests.post('https://www.biblegateway.com/newsletters/subscribe/', data=data1)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.biblegateway.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, "biblegateway.com")
        try:
            res2 = requests.post('https://www.nbc26.com/account/manage-email-preferences', data=data2)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'www.nbc26.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, "nbc26.com")
        try:
            res3 = requests.post('https://api.ewscloud.com/prod/notifications/v1/wgba/contactlists/subscribe/', data=data3)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'ewscloud.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, 'ewscloud.com')
        try:
            res4 = requests.post('https://activation.healthline.com/api/activate/site', data=data4)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'healthline.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, 'healthline.com')
        try:
            res5 = requests.post('https://api.click2houston.com/sailthru/sailthru/updatelists/new', data=data5)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'click2houston.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, 'click2houston.com')
        try:
            res6 = requests.post('https://www.cbsnews.com/newsletters/xhr/signup', data=data6)
            print(Fore.GREEN + '> ' + Style.RESET_ALL + 'Sucessfully subscribed ' + Fore.CYAN + '{} '.format(email) + Style.RESET_ALL + 'to ' + Fore.CYAN + 'cbsnews.com')
            sleep(0.25)
        except Exception as e:
            error(e.message, 'cbsnews.com')
    except KeyboardInterrupt:
        exit()

if __name__ == '__main__':
    login()
    for email in valid_emails:
        if valid_emails_count == 0:
            print(Fore.RED + '> ' + Style.RESET_ALL + f"Aborting.")
            break
        else:
            main(email)