import os
import sys
import socket as sk
from colorama import Style,Fore,Back

def title_install():
	os.system("apt install openssh && pip2 install socket && apt install systemctl")
	os.system("apt install toilet && toilet Package Installed")
	os.system("pip2 install colorama && toilet Module Installed")
	os.system("apt install tor && figlet Tor Installed")
	os.system("apt install figlet && figlet Hax4Us")
	
def code_bn():
	main_ip=(sk.gethostbyname(sk.gethostname()))
	choose=(input("1.Start Tor"+" 2.DDOS Botnet"+" 0.Exit"))
	if choose==("1"):
		os.system("sudo systemctl start tor.service")
	else:
		print("Error")
code_bn()
