# @DegGixM & @DejavuTeam & @DejavuSupport.
#!/bin/env python3

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import configparser
import os, sys
import csv
import traceback
import time
import random

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
             ╭━━━╮ 
             ╰╮╭╮┃╱╱╭╮
             ╱┃┃┃┣━━╋╋━━┳╮╭┳╮╭╮
             ╱┃┃┃┃┃━╋┫╭╮┃╰╯┃┃┃┃
            ╭╯╰╯┃┃━┫┃╭╮┣╮╭┫╰╯┃
            ╰━━━┻━━┫┣╯╰╯╰╯╰━━╯
            ╱╱╱╱╱╱╭╯┃
            ╱╱╱╱╱╱╰━╯
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            versiya : 3.1
	    @DegGixM & @DejavuTeam & @DejavuSupport
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re+"[!] əvvəlcə python setup.py proqramını işə salın !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Kodu daxil edin: '+re))
 
os.system('clear')
banner()
input_file = sys.argv[1]
users = []
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)
 
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
i=0
for group in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+group.title)
    i+=1

print(gr+'[+] Üzvlər əlavə etmək üçün qrup seçin')
g_index = input(gr+"[+] Nömrə daxil edin : "+re)
target_group=groups[int(g_index)]
 
target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
 
print(gr+"[1] istifadəçi ID-si ilə üzv əlavə edin\n[2] istifadəçi adı ilə üzv əlavə edin ")
mode = int(input(gr+"Input : "+re)) 
n = 0
 
for user in users:
    n += 1
    if n % 50 == 0:
	    time.sleep(1)
	    try:
	        print ("Əlavə edilir {}".format(user['id']))
	        if mode == 1:
	            if user['username'] == "":
	                continue
	            user_to_add = client.get_input_entity(user['username'])
	        elif mode == 2:
	            user_to_add = InputPeerUser(user['id'], user['access_hash'])
	        else:
	            sys.exit(re+"[!] Yanlış Rejim Seçildi. Zəhmət olmasa bir daha cəhd edin.")
	        client(InviteToChannelRequest(target_group_entity,[user_to_add]))
	        print(gr+"[+] 5-10 Saniyə gözləyin...")
	        time.sleep(random.randrange(5, 10))
	    except PeerFloodError:
	        print(re+"[!] Telegramdan Daşqın Xətası Alınır. \n[!] Skript indi dayanır. \n[!] Bir müddət sonra yenidən cəhd edin.")
	    except UserPrivacyRestrictedError:
	        print(re+"[!] İstifadəçinin məxfilik parametrləri bunu etməyə imkan vermir. Atlama.")
	    except:
	        traceback.print_exc()
	        print(re+"[!] Gözlənilməz Xəta")
	        continue
