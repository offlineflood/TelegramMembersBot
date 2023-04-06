# @DegGixM & @DejavuTeam & @DejavuSupport.
#!/bin/env python

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import configparser
import os, sys
import csv
import random
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
SLEEP_TIME = 30

class main():

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

    def send_sms():
        try:
            cpass = configparser.RawConfigParser()
            cpass.read('config.data')
            api_id = cpass['cred']['id']
            api_hash = cpass['cred']['hash']
            phone = cpass['cred']['phone']
        except KeyError:
            os.system('clear')
            main.banner()
            print(re+"[!] əvvəlcə python setup.py proqramını işə salın !!\n")
            sys.exit(1)

        client = TelegramClient(phone, api_id, api_hash)
         
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            os.system('clear')
            main.banner()
            client.sign_in(phone, input(gr+'[+] Kodu daxil edin: '+re))
        
        os.system('clear')
        main.banner()
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
        print(gr+"[1] istifadəçi ID ilə sms göndər\n[2] istifadəçi adı ilə sms göndər ")
        mode = int(input(gr+"Input : "+re))
         
        message = input(gr+"[+] Mesajınızı daxil edin : "+re)
         
        for user in users:
            if mode == 2:
                if user['username'] == "":
                    continue
                receiver = client.get_input_entity(user['username'])
            elif mode == 1:
                receiver = InputPeerUser(user['id'],user['access_hash'])
            else:
                print(re+"[!] Yanlış Rejim. Çıxılır.")
                client.disconnect()
                sys.exit()
            try:
                print(gr+"[+] Mesaj göndərilir:", user['name'])
                client.send_message(receiver, message.format(user['name']))
                print(gr+"[+] {} saniyə gözləyir".format(SLEEP_TIME))
                time.sleep(SLEEP_TIME)
            except PeerFloodError:
                print(re+"[!] Telegramdan Daşqın Xətası Alınır. \n[!] Skript indi dayanır. \n[!] Bir müddət sonra yenidən cəhd edin.")
                client.disconnect()
                sys.exit()
            except Exception as e:
                print(re+"[!] Xəta:", e)
                print(re+"[!] Davam etməyə çalışır...")
                continue
        client.disconnect()
        print("Bitdi. Mesaj bütün istifadəçilərə göndərildi.")



main.send_sms()
