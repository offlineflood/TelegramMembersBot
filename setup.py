# @DegGixM & @DejavuTeam & @DejavuSupport.

"""
setup.py-ni yenidən işə sala bilərsiniz
bəzi səhv dəyər əlavə etmisinizsə
"""
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴
	""")

def requirements():
	def csv_lib():
		banner()
		print(gr+'['+cy+'+'+gr+']'+cy+' this may take some time ...')
		os.system("""
                          pip cython numpy pandaları quraşdırın
                          python -m pip quraşdırma cython numpy pandas
			""")
	banner()
	print(gr+'['+cy+'+'+gr+']'+cy+' csv birləşməsini quraşdırmaq 10 dəqiqə çəkəcək.')
	input_csv = input(gr+'['+cy+'+'+gr+']'+cy+' csv birləşməsini aktiv etmək istəyirsiniz (y/n): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(gr+"[+] Quraşdırma tələbləri ...")
	os.system("""
		pip konfiqurasiya analizatorunu quraşdırın
                python -m pip quraşdırma teleton sorğuları konfiqurasiya analizatoru
                config.data-ya toxunun
		""")
	banner()
	print(gr+"[+] tələblər quraşdırılıb.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(gr+"[+] API ID daxil edin : "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(gr+"[+] HASH ID daxil edin : "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(gr+"[+] telefon nömrəsini daxil edin : "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"[+] quraşdırma tamamlandı !")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(gr+'['+cy+'+'+gr+']'+cy+' birləşmə '+sys.argv[2]+' & '+sys.argv[3]+' ...')
	print(gr+'['+cy+'+'+gr+']'+cy+' böyük fayllar bir az vaxt ala bilər ... ')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'['+cy+'+'+gr+']'+cy+' faylı "output.csv" kimi saxladı\n')

def update_tool():
	import requests as r
	banner()
	source = r.get("https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/.image/.version")
	if source.text == '3':
		print(gr+'['+cy+'+'+gr+']'+cy+' artıq son versiya')
	else:
		print(gr+'['+cy+'+'+gr+']'+cy+' köhnə faylları silmək ...')
		os.system('rm *.py');time.sleep(3)
		print(gr+'['+cy+'+'+gr+']'+cy+' ən son faylları əldə etmək ...')
		os.system("""
			curl -s -O https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/add2group.py
			curl -s -O https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/scraper.py
			curl -s -O https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/setup.py
			curl -s -O https://raw.githubusercontent.com/offlineflood/TelegramMembersBot/master/smsbot.py
			chmod 777 *.py
			""");time.sleep(3)
		print(gr+'\n['+cy+'+'+gr+']'+cy+' yeniləmə tamamlandı.\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(gr+'['+cy+'+'+gr+']'+cy+' seçilmiş modul : '+re+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		print(gr+'['+cy+'+'+gr+']'+cy+' seçilmiş modul : '+re+sys.argv[1])
		merge_csv()
	elif any ([sys.argv[1] == '--update', sys.argv[1] == '-u']):
		print(gr+'['+cy+'+'+gr+']'+cy+' seçilmiş modul : '+re+sys.argv[1])
		update_tool()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""$ python setup.py -m file1.csv file2.csv
			
	( --config  / -c ) api konfiqurasiyasını quraşdırın
	( --merge   / -m ) 2 .csv faylını birində birləşdirin 
	( --update  / -u ) aləti ən son versiyaya yeniləyin
	( --install / -i ) quraşdırma tələbləri
	( --help    / -h ) bu mesajı göstər 
			""")
	else:
		print('\n'+gr+'['+re+'!'+gr+']'+cy+' naməlum arqument : '+ sys.argv[1])
		print(gr+'['+re+'!'+gr+']'+cy+' kömək istifadə üçün : ')
		print(gr+'$ python setup.py -h'+'\n')
except IndexError:
	print('\n'+gr+'['+re+'!'+gr+']'+cy+' heç bir arqument verilməmişdir : '+ sys.argv[1])
	print(gr+'['+re+'!'+gr+']'+cy+' kömək istifadə üçün : ')
	print(gr+'['+re+'!'+gr+']'+cy+' https://github.com/offlineflood/TelegramMembersBot#-how-to-install-and-use')
	print(gr+'$ python setup.py -h'+'\n')
