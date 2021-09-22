#!/usr/bin/env python
# coding: utf-8
# By Sandaru Ashen: https://github.com/Sl-Sanda-Ru

import random
import os
import time
import sys
import pip

try:
    import requests
    import colorama
    import pyfiglet
except ModuleNotFoundError:
    print('\x1b[1m\x1b[31m' + '[!] required dependencies aren\'t installed\ninstalling..'.title())
    pip.main(['install', 'pyfiglet', 'colorama', 'requests'])
    sys.exit('\x1b[1m\x1b[92m' + '[+] dependencies installed\nrun the program again'.title())


BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
NUMS = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
LETTS = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
color_list = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
CLEAR = 'cls' if os.name == 'nt' else 'clear'
FONTS = 'basic', 'o8', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
colorama.init(autoreset=True)

def authreq(num, method):
    json = {'countryCode':'', 'dialingCode':None, 'installationDetails':{'app':{'buildVersion':5, 'majorVersion':11, 'minorVersion':75, 'store':'GOOGLE_PLAY'}, 'device':{'deviceId':''.join(random.choices(NUMS+LETTS, k=16)), 'language':'en', 'manufacturer':'Xiaomi', 'mobileServices':['GMS'], 'model':'M2010J19SG', 'osName':'Android', 'osVersion':'10', 'simSerials':[''.join(random.choices(NUMS, k=19)), ''.join(random.choices(NUMS, k=20))]}, 'language':'en', 'sims':[{'imsi':''.join(random.choices(NUMS, k=15)), 'mcc':'413', 'mnc':'2', 'operator':None}]}, 'phoneNumber':num, 'region':'region-2', 'sequenceNo':''}
    headers = {'content-type':'application/json; charset=UTF-8', 'accept-encoding':'gzip', 'user-agent':'Truecaller/11.75.5 (Android;10)', 'clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'}
    if method == 'call':
        json['sequenceNo'] = 1
    else:
        json['sequenceNo'] = 2
    req = requests.post('https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp', headers=headers, json=json)
    if req.json()['status'] == 1 or req.json()['status'] == 9:
        return req.json()['requestId']
    else:
        return False, req.json()['message']

def authveri(id, num, pin):
    json = {'countryCode':'', 'dialingCode':None, 'phoneNumber':num, 'requestId':id, 'token':pin}
    headers = {'content-type':'application/json; charset=UTF-8', 'accept-encoding':'gzip', 'user-agent':'Truecaller/11.75.5 (Android;10)', 'clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'}
    req = requests.post('https://account-asia-south1.truecaller.com/v1/verifyOnboardingOtp', headers=headers, json=json)
    if req.json()['status'] == 11:
        return False, 'OTP code is invalid'
    elif req.json()['status'] == 2 and req.json()['suspended']:
        return False, 'oops.. your account got suspended. try another number :('
    else:
        return req.json()['installationId']

def numsearch(authkey,num):
    params = {'q':num, 'countryCode':'', 'type':'4', 'locAddr':'', 'placement':'SEARCHRESULTS,HISTORY,DETAILS', 'encoding':'json'}
    headers = {'content-type':'application/json; charset=UTF-8', 'accept-encoding':'gzip', 'user-agent':'Truecaller/11.75.5 (Android;10)', 'clientsecret':'lvc22mp3l1sfv6ujg83rd17btt', 'authorization':'Bearer ' + authkey}
    req = requests.get('https://search5-noneu.truecaller.com/v2/search', headers=headers, params=params)
    if req.json().get('status'):
        return False, 'your authorization key is expired, please login again'
    else:
        return req.json()
def logo():
    os.system(CLEAR)
    font = random.choice(FONTS)
    color1 = random.choice(color_list)
    color2 = random.choice(color_list)
    while color1 == color2:
        color2 = random.choice(color_list)
    print('\n' * 2 + color2 + pyfiglet.figlet_format('Truecaller\nCLI', font=font, justify='center', width=os.get_terminal_size().columns), end='\n')
def spinner():
    l = ['|','/','-','\\']
    tmp = '[*] checking your internet connection'.title().center(os.get_terminal_size().columns).split('[*] checking your internet connection'.title())[0]
    _ = random.choice(color_list)
    for i in l + l + l:
        sys.stdout.write('\r' + tmp + _ + '[*] checking your internet connection   '.title() + random.choice(color_list) + i)
        time.sleep(0.2)
    print('')
def main():
    logo()
    try:
        file = open('.auth')
    except FileNotFoundError:
        creds = False
    else:
        tmp = file.read()
        file.close()
        creds = {'auth':tmp.split(',')[0],'num':tmp.split(',')[1]}
    tmp = '>>> '.title().center(os.get_terminal_size().columns).split('>>> ')[0]
    if creds:
        print(random.choice(color_list) + f'welcome you are logged in as {creds["num"]}'.title().center(os.get_terminal_size().columns))
        print(LICYA + '1.search'.title().center(os.get_terminal_size().columns))
        print(LIYEL + '2.login'.title().center(os.get_terminal_size().columns))
        print(RED + '3.exit'.title().center(os.get_terminal_size().columns))
        while True:
            try:
                selected = int(input(colorama.Style.BRIGHT + tmp[:-3] + '>>> '))
                if selected in range(1,4):
                    break
                else:
                    print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
            except ValueError:
                print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
    else:
        print(LIYEL + '1.login (you must login via mobile number first)'.title().center(os.get_terminal_size().columns))
        print(RED + '2.exit'.title().center(os.get_terminal_size().columns))
        while True:
            try:
                selected = int(input(colorama.Style.BRIGHT + tmp[:-3] + '>>> '))
                if selected in range(1,3):
                    break
                else:
                    print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
            except ValueError:
                print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
    if creds is False and selected == 1 or creds and selected == 2:
        logo()
        print(random.choice(color_list) + '[+] enter your phone number in international format with plus sign'.title().center(os.get_terminal_size().columns))
        print(random.choice(color_list) + 'example: +16462033216'.title().center(os.get_terminal_size().columns))
        while True:
            unum = input(colorama.Style.BRIGHT + tmp[:-3] + '>>> ')
            if len(unum) > 7 and unum[0] == '+' and unum[1:].isdecimal():
                break
            else:
                print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
        while True:
            print(random.choice(color_list) + '[+] enter your verification method (call/sms)'.title().center(os.get_terminal_size().columns))
            method = input(colorama.Style.BRIGHT + tmp[:-3] + '>>> ')
            if method.lower() in ('sms', 'call'):
                break
            else:
                print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
        result = authreq(unum, method.lower())
        time.sleep(1)
        if isinstance(result, tuple):
            print(RED + f'[!] {result[1]}'.title().center(os.get_terminal_size().columns))
            input(random.choice(color_list) + 'press <enter> to go to main menu'.title().center(os.get_terminal_size().columns))
            main()
        else:
            print(LIGRE + f'[+] Sent An OTP {unum}'.center(os.get_terminal_size().columns))
            time.sleep(1)
            logo()
            print(random.choice(color_list) + '[+] Enter Your Received OTP Code'.center(os.get_terminal_size().columns))
            while True:
                otp = input(colorama.Style.BRIGHT + tmp[:-3] + '>>> ')
                if otp.isdecimal():
                    break
                else:
                    print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
            result = authveri(result, unum, otp)
            if isinstance(result, tuple):
                print(RED + f'[!] {result[1]}'.title().center(os.get_terminal_size().columns))
                input(random.choice(color_list) + 'press <enter> to go to main menu'.title().center(os.get_terminal_size().columns))
                main()
            else:
                print(GRE + f'[+] logged in as {unum}'.title().center(os.get_terminal_size().columns))
                with open('.auth','w') as file:
                    file.write('%s,%s'%(result,unum))
                time.sleep(1)
                main()
    elif creds and selected == 1:
        print(random.choice(color_list) + '[+] enter your phone number that you want to search'.title().center(os.get_terminal_size().columns))
        print(random.choice(color_list) + 'in international format with plus sign'.title().center(os.get_terminal_size().columns))
        while True:
            lnum = input(colorama.Style.BRIGHT + tmp[:-3] + '>>> ')
            if len(lnum) > 7 and lnum[0] == '+' and lnum[1:].isdecimal():
                break
            else:
                print(RED + '[!] wrong input'.title().center(os.get_terminal_size().columns))
        tmp2 = numsearch(creds['auth'], lnum)
        if isinstance(tmp2, tuple):
            print(LIRED + f'[!] {tmp2[1]}'.title().center(os.get_terminal_size().columns))
            input(random.choice(color_list) + 'press <enter> to go to main menu'.title().center(os.get_terminal_size().columns))
            main()
        else:
            country = requests.get('https://restcountries.com/v2/callingcode/' + str(tmp2['data'][0]['phones'][0]['dialingCode'])).json()[0]['name']
            if tmp2['data'][0]['phones'][0]['numberType'] == 'UNKNOWN':
                print(LIRED + f'[!] not a valid number in country {country}'.title().center(os.get_terminal_size().columns))
                input(random.choice(color_list) + 'press <enter> to go to main menu'.title().center(os.get_terminal_size().columns))
                main()
            if tmp2['data'][0].get('name'):
                print(random.choice(color_list) + f"Name: {tmp2['data'][0]['name']}".title().center(os.get_terminal_size().columns))
            else:
                print(LIRED + 'name not found in the databse'.title().center(os.get_terminal_size().columns))
            if tmp2['data'][0].get('gender'):
                print(random.choice(color_list) + f"Gender: {tmp2['data'][0]['gender']}".title().center(os.get_terminal_size().columns))
            if tmp2['data'][0]['phones'][0].get('countryCode'):
                print(random.choice(color_list) + f"Country: {country}".title().center(os.get_terminal_size().columns))
            if tmp2['data'][0]['phones'][0].get('numberType'):
                print(random.choice(color_list) + f"Number Type: {tmp2['data'][0]['phones'][0]['numberType']}".title().center(os.get_terminal_size().columns))
            if tmp2['data'][0]['phones'][0].get('carrier'):
                print(random.choice(color_list) + f"Carrier: {tmp2['data'][0]['phones'][0]['carrier']}".title().center(os.get_terminal_size().columns))
            if tmp2['data'][0]['internetAddresses']:
                print(random.choice(color_list) + f"Email: {tmp2['data'][0]['internetAddresses'][0]['id']}".title().center(os.get_terminal_size().columns))
            input(random.choice(color_list) + 'press <enter> to go to main menu'.title().center(os.get_terminal_size().columns))
            main()
    else:
        sys.exit()




if __name__ == '__main__':
    logo()
    spinner()
    try:
        requests.get('https://github.com/')
        time.sleep(0.4)
        print(LIGRE + '[+] Connection Successful!'.center(os.get_terminal_size().columns))
        time.sleep(0.4)
    except Exception:
        time.sleep(0.4)
        print(LIRED + '[!] Connection Failed!'.center(os.get_terminal_size().columns))
        time.sleep(0.4)
        sys.exit(LIRED + '[!] Exiting'.center(os.get_terminal_size().columns))
    main()
