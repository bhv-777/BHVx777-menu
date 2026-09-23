#--------|
#MODÜLLER|
#--------|
import requests
import os
import time
import pyfiglet
import sys



#-------|
#RENKLER|
#-------|
KIRMIZI = "\033[91m"
YESIL   = "\033[92m"
SARI    = "\033[93m"
MAVI    = "\033[94m"
MOR     = "\033[95m"
CYAN    = "\033[96m"
BEYAZ   = "\033[97m"
GRI     = "\033[90m"
RESET   = "\033[0m"



#-----|
#GIRIS|
#-----|
os.system("clear")
os.system("pkg update && pkg upgrade -y")
os.system("pkg install aapt2")
os.system("pkg install python3")
os.system("clear")
print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎{RESET}")
F = pyfiglet.figlet_format("BHVx777")
print(f"{CYAN}{F}{RESET}")
print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎{RESET}\n") #Aga giriş müq oldu aq
yazi = f"""{KIRMIZI}Girişe tıklayarak şunları kabul etmiş olursunuz:	
{RESET}\n{SARI}Yetkisiz kullanım YASA DIŞIDIR ve ağır cezai yaptırımları vardır
Bu aracı kullanarak yapacağınız her türlü işlemin sorumluluğu TAMAMEN SİZE AİTTİR
Kötü niyetli kullanım asla desteklenmez{RESET}\n
"""
for char in yazi:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎\n{RESET}")
time.sleep(3)
input(f"{YESIL}Enter'a basarak devam edin{RESET}")
os.system("clear")
print(f"{SARI}Bitmek üzere...{RESET}")
time.sleep(3)
os.system("clear")
print(f"{KIRMIZI}Bitti{RESET}")
time.sleep(2.5)
os.system("clear")



#----|
#MENU|
#----|
def menu():
	print(f"""{KIRMIZI}
 ███████████  █████   █████ █████   █████             ██████████ ██████████ ██████████
░░███░░░░░███░░███   ░░███ ░░███   ░░███             ░███░░░░███░███░░░░███░███░░░░███
 ░███    ░███ ░███    ░███  ░███    ░███  █████ █████░░░    ███ ░░░    ███ ░░░    ███ 
 ░██████████  ░███████████  ░███    ░███ ░░███ ░░███       ███        ███        ███  
 ░███░░░░░███ ░███░░░░░███  ░░███   ███   ░░░█████░       ███        ███        ███   
 ░███    ░███ ░███    ░███   ░░░█████░     ███░░░███     ███        ███        ███    
 ███████████  █████   █████    ░░███      █████ █████   ███        ███        ███     
░░░░░░░░░░░  ░░░░░   ░░░░░      ░░░      ░░░░░ ░░░░░   ░░░        ░░░        ░░░      
                                                                                      
                                                                                      
                                                                                      
{RESET}""")
	print(f"{YESIL}Mehraba BHVx777 menüsüne hoşgeldiniz burda seçiminizi başlarındaki sayı ile girin{RESET}\n")
	print(f"{YESIL}██████████████████████████████████████████████████████████{RESET}")
	print(f"{SARI}Geliştirici:{RESET}{MOR}	 BHV{RESET}")
	print(f"{YESIL}██████████████████████████████████████████████████████████{RESET}")
	print(f"{KIRMIZI}[1]{RESET}{CYAN}\tngrok tüne'li aç{RESET}")
	print(f"{KIRMIZI}[2]{RESET}{CYAN}\tAPK izinleri tara{RESET}")
	print(f"{KIRMIZI}[3]{RESET}{CYAN}\tZphisher aç (phising){RESET}")
	print(f"{KIRMIZI}[4]{RESET}{CYAN}\tDDOS saldırısı yap{RESET}")
	print(f"{KIRMIZI}[5]{RESET}{CYAN}\tWeb site parametre saldırısı yap{RESET}")
	print(f"{KIRMIZI}[6]{RESET}{CYAN}\tWeb site GET isteği at (Site dinle){RESET}")
	print(f"{KIRMIZI}[7]{RESET}{CYAN}\tWeb site gizli parametre'lerini bul (sadece php){RESET}")
	print(f"{KIRMIZI}[8]{RESET}{CYAN}\tGÜNCELLE/UPDATE{RESET}")
	print(f"{KIRMIZI}[99]{RESET}{CYAN}\tExit{RESET}")
	print(f"{YESIL}██████████████████████████████████████████████████████████{RESET}")


#---|
#KÖK|
#---|
while True:
	menu()
	secim = input(f"{SARI}Seçminiz:    {RESET}")
	if secim == "1":
		os.system("clear")
		f = pyfiglet.figlet_format("NGROK")
		print(f"{MAVI}{f}{RESET}")
		s = input(f"{SARI}Hangi port ile tünel açılacak:    {RESET}")
		os.system("clear")
		tunel = f"{CYAN}Tünel oluşturuluyor...{RESET}"
		for karakter in tunel:
		    sys.stdout.write(karakter)
		    sys.stdout.flush()
		    time.sleep(0.05)
		time.sleep(3)
		os.system("clear")
		os.system(f"ngrok http {s}")
		input(f"{SARI}Devam etmek için Enter'a tıklayın{RESET}")
		os.system("clear")
	elif secim == "2":
		os.system("clear")
		aapt = pyfiglet.figlet_format("APK PERMISSIONS")
		print(f"{MAVI}{aapt}{RESET}")
		yol = os.path.expanduser("~/storage/downloads/")
		os.chdir(yol)
		os.system("ls")
		se = input(f"{SARI}Seçmek istediğiniz APK'nın adını girin:    {RESET}")
		os.system("clear")
		Not = f"{CYAN}Not: bu seçenek APK'ların{RESET} {MOR}AndroidManifest.xml{RESET} {CYAN}izinlerine tarar{RESET}"
		for bilgi in Not:
		    sys.stdout.write(bilgi)
		    sys.stdout.flush()
		    time.sleep(0.05)
		time.sleep(3.9)
		os.system(f"aapt2 dump permissions {se}")
		input(f"{SARI}Devam etmek için Enter'a tıklayın{RESET}\n")
		os.system("clear")
	elif secim == "3":
		zf = pyfiglet.figlet_format("ZPHISHER")
		print(f"{MAVI}zf{RESET}")
		os.system("clear")
		sec = input(f"{SARI}Sizde Zphisher adlı Tool varmı{RESET}{MAVI}[Y/N]{RESET}:	")
		os.system("clear")
		if sec == "y":
			zph = os.path.expanduser("~/zphisher/")
			os.chdir(zph)
			os.system("bash zphisher.sh")
			os.system("clear")
		elif sec == "n":
			zs = input(f"{SARI}Zphisher Tool'u yüklensinmi{RESET}{MAVI}[Y/N]{RESET}:	")
			if zs == "y":
				os.system("pkg install git")
				os.system("git clone https://github.com/htr-tech/zphisher")
				os.system("cd zphisher")
				os.system("bash zphisher.sh")
				os.system("clear")
			elif zs == "n":
				os.system("clear")
	elif secim == "4":
		os.system("clear")
		df = pyfiglet.figlet_format("DDOS")
		print(f"{MAVI}{df}{RESET}")
		dds = input(f"{SARI}Sizde {RESET}{MOR}DDoS-Ripper{RESET} {SARI}adlı tool varmı{RESET} {MAVI}[Y/N]{RESET}:    ")
		if dds == "y":
			dsi = input(f"{SARI}ddos atmak istediğiniz IP adresini girin{RESET}:    ")
			dps = input(f"{SARI}ddos atmak istediğiniz sitenin açık port'unu biliyormusunuz{RESET}{MAVI}[Y/N]{RESET}:    ")
			if dps == "y":
				dy = os.path.expanduser("~/DDoS-Ripper/")
				os.chdir(dy)
				dsp = input(f"{SARI}Sitenin açık port'unu girin{RESET}:    ")
				os.system(f"python3 DRipper.py -s {dsi} -p {dsp} -t 135")
				input(f"{KIRMIZI}DDOS{RESET} {CYAN}saldırısı bitmiştir devam etmek için enter'a tıklayın{RESET}")
				os.system("clear")
			elif dps == "n":
				dys = os.path.expanduser("~/DDoS-Ripper/")
				os.chdir(dys)
				dsi2 = input(f"{SARI}ddos atmak istediğiniz IP adresini girin{RESET}:    ")
				os.system("python3 DRipper.py -s {dsi2} -t 135")
				input(f"{KIRMIZI}DDOS{RESET} {CYAN}saldırısı bitmiştir devam etmek için enter'a tıklayın{RESET}")
				os.system("clear")
		elif dds == "n":
			dty = pyfiglet.figlet_format("INSTALLING")
			print(f"{MAVI}{dty}{RESET}")
			os.system("pkg install git -y && pkg install python3 && git clone https://github.com/palahsu/DDoS-Ripper.git && cd DDoS-Ripper")
			input(f"{MOR}DDoS-Ripper{RESET} {CYAN}adlı tool BHVx777 klasörüne yüklendi devam etmek için enter'a tıklayın{RESET}")
			os.system("clear")
	elif secim == "5":
		os.system("clear")
		gd = pyfiglet.figlet_format("Parametre\nAttacks")
		print(f"{MAVI}{gd}{RESET}")
		print(f"{CYAN}Başlarındaki sayı ile belirtin{RESET}")
		print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪{RESET}")
		print(f"{KIRMIZI}[1]{RESET}	{CYAN}Gobuster{RESET}") #istediğin txt deneyebilirsin gelişmiş
		print(f"{KIRMIZI}[2]{RESET}	{CYAN}Dirb{RESET}") #Eski ve özel bir txt kullanılamaz
		print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪{RESET}\n")
		gdn = f"{MOR}Not{RESET}: {CYAN}Gobuster'de kendi txt kullanabiliyorsun{RESET}\n\n"
		for ndg in gdn:
		    sys.stdout.write(ndg)
		    sys.stdout.flush()
		    time.sleep(0.05)
		print(f"{KIRMIZI}▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪︎▪{RESET}\n")
		gds = input(f"{SARI}Seçiminiz:    {RESET}")
		gdy = input(f"{MOR}Gobuster {YESIL}ve {RESET}{MOR}Dirb{RESET} {YESIL}sizde yüklümü{RESET}{MAVI}[Y/N]{RESET}:    ")
		if gdy == "y":
			if gds == "1":
				os.system("clear")
				gs = input(f"{SARI}Sitenin Link'nini girin{RESET}:    ")
				gt = input(f"{SARI}Kendi txt'iniz belirtmek istermisiniz{RESET}{MAVI}[Y/N]:    ")
				if gt == "y":
					gts = input(f"{SARI}txt ismini belirtiniz{RESET}:    ")
					os.system("clear")
					print(f"{CYAN}Başlatılıyor...{RESET}")
					time.sleep(3)
					os.system("clear")
					os.system(f"gobuster dir -u {gs} -w ~/{gts}")
					input(f"{YESIL}Devam etmek için enter'a bas{RESET}")
					os.system("clear")
				elif gt == "n":
					os.system("clear")
					print(f"{CYAN}Başlatılıyor...{RESET}")
					time.sleep(3)
					os.system("clear")
					os.system(f"gobuster dir -u {gs} -w ~/common.txt")
					input(f"{YESIL}Devam etmek için enter'a bas{RESET}")
					os.system("clear")
			elif gds == "2":
				os.system("clear")
				ds = input(f"{SARI}Sitenin Link'nini girin{RESET}:    ")
				os.system("clear")
				print(f"{CYAN}Başlatılıyor...{RESET}")
				time.sleep(3)
				os.system("clear")
				os.system(f"dirb {ds}")
				input(f"{YESIL}Devam etmek için enter'a basın{RESET}")
				os.system("clear")
		elif gdy == "n":
			os.system("pkg install golang -y && go install github.com/OJ/gobuster/v3@latest && export PATH=$PATH:~/go/bin && echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc")
			os.system("pkg install dirb")
			input(f"{YESIL}Yükleme bitti enter'a basarak devam edin")
			os.system("clear")
	elif secim == "6":
		os.system("clear")
		rs = pyfiglet.figlet_format("GET WEBSITE")
		print(f"{MAVI}{rs}{RESET}")
		gas = input(f"{SARI}GET atılacak site giriniz{RESET}:    ")
		r = requests.get(f"{gas}")
		print(r.status_code)
		print(r.text)
		input(f"{SARI}Devam etmek için enter'a tıklayın{RESET}")
		os.system("clear")
	elif secim == "7":
		os.system("clear")
		arjun = pyfiglet.figlet_format("GIZLI PARAMETRELER")
		print(f"{MAVI}{arjun}{RESET}")
		ay = input(f"{SARI}sizde {RESET}{MOR}arjun{RESET} {SARI}yüklümü{RESET}{MAVI}[Y/N]{RESET}:    ")
		if ay == "y":
			As = input(f"{SARI}Hedef site{RESET}:    ")
			os.system(f"arjun -u {As}")
			input(f"{SARI}Devam etmek için enter'a tıklayın{RESET}")
			os.system("clear")
		elif ay == "n":
			os.system("pip install arjun")
			input(f"{MOR}arjun {RESET}{SARI}yüklendi devam etmek için enter'a tıklayın{RESET}:    ")
			os.system("clear")
	elif secim == "8":
		os.system("clear")
		Güncelle = pyfiglet.figlet_format("GUNCELLE\n/\nUPDATE")
		print(f"{MAVI}{Güncelle}{RESET}")
		os.system("pkg install git")
		GY = os.path.expanduser("/data/data/com.termux/files/home")
		os.chdir(GY)
		os.system("rm -rf BHVx777-menu")
		input(f"{SARI}DEVAM ET{RESET}")
		os.system("git clone https://github.com/bhv-777/BHVx777-menu.git")
		input(f"{SARI}Enter'a basarak yaapılacak adımları izleyin{RESET}")
		GN = f"{CYAN}Aşağıdaki komutu kopyalayın ve terminalinize yapıştırarak çalıştırın{RESET}\n\n{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{RESET}\n\ncd && cd BHVx777-menu && python bhv.py\n\n{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n\n{CYAN}Komutu çalıştırmadan önce menüden çıkın 99 yapın{RESET}\n\n{YESIL}■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■{RESET}\n\n"
		for güncelleNot in GN:
		    sys.stdout.write(güncelleNot)
		    sys.stdout.flush()
		    time.sleep(0.05)
		time.sleep(3.5)
		input(f"{YESIL}Devam etmek için enter'a basın{RESET}")
		os.execv(sys.executable, [sys.executable, os.path.join(GY, "BHVx777-menu", "main.py")])
		os.system("clear")




