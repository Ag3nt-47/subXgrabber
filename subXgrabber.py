import requests
import threading
from languages import *
from my_colors import *
import os

print_lock = threading.Lock()


def send_req(lang, subdomain):
    try:
        url = f"http://{subdomain}.{target_site}"
        response = requests.get(url)
        if str(response.status_code).startswith("2"):
            success = f"{subdomain}.{target_site}"
            success_list.append(success)
            with print_lock:
                if language == 'en':
                    print(f"{fg}Successfull: {fw}{success}")
                elif language == 'nl':
                    print(f"{fg}Succesvol: {fw}{success}")
                elif language == 'ru':
                    print(f"{fg}Успешный: {fw}{success}")
                elif language == 'tr':
                    print(f"{fg}Başarılı: {fw}{success}")
                elif language == 'pl':
                    print(f"{fg}Udany: {fw}{success}")
    except:
        pass


ascii_name = f'''{fg}

 @@@@@@    @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@       @@@   @@@@@@@@
@@@@@@@@  @@@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@@@@      @@@@   @@@@@@@@
@@!  @@@  !@@        @@!       @@!@!@@@    @@!       @@!@!        @@!
!@!  @!@  !@!        !@!       !@!!@!@!    !@!      !@!!@!       !@!
@!@!@!@!  !@! @!@!@  @!!!:!    @!@ !!@!    @!!     @!! @!!      @!!
!!!@!!!!  !!! !!@!!  !!!       !@!  !!!    !!!    !!!  !@!     !!!
!!:  !!!  :!!   !!:  :!:       !!:  !!!    !!:    :!!:!:!!:   !!:
:!:  !:!  :::: ::::  :: ::::   :!:  !:!    :!:         :::    :!:
'''

ascii_tool = f'''{fr}
                         \ / _
                 _    |_  X (_| __ _ |_ |_  _  __                                    
                _> |_||_)/ \__| | (_||_)|_)(/_ |
'''
print(ascii_name, end='')
print(ascii_tool)


language = input(
    f"{fw}Which language you using? {fw}({fb}en{fw}/{fr}n{fbb}l{fw}/{fw}r{fbb}u{fw}/{fr}t{fw}r{fw}/{fw}p{fr}l{fw})\n")
language = language.lower()
print_choose(lang=language)

input_wordlist = input(f"{fg}1{fw}/{fy}2{fw}/{fr}3{fw}/{black}4{fw}: ")
print()

try:
    input_wordlist = int(input_wordlist)
except:
    sys.exit()

if get_operating_system() == "Windows":
    if input_wordlist == 1:
        input_wordlist = r'wordlists\fast-wordlist.txt'
    elif input_wordlist == 2:
        input_wordlist = r'wordlists\normal-wordlist.txt'
    elif input_wordlist == 3:
        input_wordlist = r'wordlists\hard-wordlist.txt'
    elif input_wordlist == 4:
        input_wordlist = r'wordlists\monster-wordlist.txt'
    else:
        sys.exit()
else:
    if input_wordlist == 1:
        input_wordlist = 'wordlists/fast-wordlist.txt'
    elif input_wordlist == 2:
        input_wordlist = 'wordlists/normal-wordlist.txt'
    elif input_wordlist == 3:
        input_wordlist = 'wordlists/hard-wordlist.txt'
    elif input_wordlist == 4:
        input_wordlist = 'wordlists/monster-wordlist.txt'
    else:
        sys.exit()



print_target(language)

target_site = input("")
if target_site.lower().startswith("http://"):
    target_site = target_site.replace("http://", "")
elif target_site.lower().startswith("https://"):
    target_site = target_site.replace("https://", "")
if target_site[-1] == '/':
    url = target_site.split('/')
    target_site = url[0]

print()

success_list = []
threads = []

with open(input_wordlist, "r") as my_wordlist:
    for subdomain in my_wordlist:
        subdomain = subdomain.strip()

        thread = threading.Thread(target=send_req, args=(language, subdomain))
        threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

file_name = str(success_list[0].split(".", 1)[1]) + ".txt"

try:
    os.mkdir('Success')
except:
    pass
try:
    os.chdir('Success')
except:
    pass

for subdomain in success_list:
    if subdomain == success_list[-1]:
        open(file_name, "a").write(subdomain)
    else:
        open(file_name, "a").write(subdomain + "\n")

exit_message(lang=language, file_name=file_name)