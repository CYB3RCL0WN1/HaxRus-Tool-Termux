import os
import sys
import socket as sk
from colorama import Style,Fore,Back

def title_install():
	os.system("apt install openssh && pip2 install socket")
	os.system("apt install toilet && toilet Package Installed")
	os.system("pip2 install colorama && toilet Module Installed")
	os.system("apt install tor && figlet Tor Installed")
	os.system("apt install figlet && apt install gay")
	os.system("apt install openssl && apt install util-linux && apt install proxychains")
title_install()
def code_bn():
	os.system("toilet -F metal Hax4Us")
	proxylist=(input(Fore.RED+"file destination for Tor Ip/Port : "+Fore.RESET))
	
	main_ip=(sk.gethostbyname(sk.gethostname()))
	choose=(input(Fore.BLUE+"1.Start Tor"+" 2.DDOS Botnet"+" 0.Exit"+":   "+Fore.RESET))
	if choose==("1"):
		os.system("tor -f "+(proxylist))
	else:
		print("Syntax Error ")
code_bn()
