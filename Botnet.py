import os
import sys
import socket as sk
from colorama import Style,Fore,Back

def title_install():
	os.system("apt install openssh && pip2 install socket")
	os.system("apt install toilet && toilet Package Installed")
	os.system("pip2 install colorama && toilet Module Installed")
	os.system("apt install tor && figlet Tor Installed")
	os.system("apt install figlet && figlet Hax4Us")
	os.system("apt install openssl && apt install torify && apt install proxychains")
	
def code_bn():
	os.system("figlet Hax4Us")
	
	main_ip=(sk.gethostbyname(sk.gethostname()))
	choose=(input(Fore.YELLOW+"1.Start Tor"+" 2.DDOS Botnet"+" 0.Exit"+":   "+Fore.RESET))
	if choose==("1"):
		os.system("tor")
	else:
		print("Error")
code_bn()
title_install()
