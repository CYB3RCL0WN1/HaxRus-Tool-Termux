import os
import sys
import socket as sk
from colorama import Style,Fore,Back

def title_install():
	os.system("apt install openssh && pip2 install socket")
	os.system("apt install toilet && toilet Package Installed")
	os.system("pip2 install colorama && toilet Module Installed")
	os.system("apt install tor && figlet Tor Installed")
	os.system("apt install figlet")
	os.system("apt install openssl && apt install util-linux")
title_install()
def code_bn():
	os.system("toilet -F metal HAX4US")
	main_ip=(sk.gethostbyname(sk.gethostname()))
	choose=(input(Fore.BLUE+"1.Start Tor"+" 2.DDOS Botnet "+"3.Edit Tor Config "+" 0.Exit"+":   "+Fore.RESET))
	if choose==("1"):
		os.system("sudo cat proxychains.conf /etc/proxychains.conf")
		os.system("sudo tor")
	if choose==("3"):
		os.system("nano /etc/proxychains.conf")
	else:
		print("Syntax Error ")
code_bn()
    
