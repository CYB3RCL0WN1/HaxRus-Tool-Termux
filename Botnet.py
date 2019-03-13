import os
import sys
import socket as sk
from colorama import Style,Fore,Back

def code_bn():
	os.system("toilet -F metal HAX4US")
	
	main_1=(Fore.BLUE+"1.Start Tor")
	main_2=("2.Start DDOS Botnet")
	main_3=("3.Edit Proxychains/Tor file(requires root)")
	main_4=("0.Exit Hax4Us"+Fore.RESET)
	print (main_1)
	print (main_2)
	print (main_3)
	print (main_4)
	Choose=input(Fore.BLUE+"choose your option:"+Fore.RESET)
	if Choose==("1"):
		os.system("sudo cat proxychains.conf /etc/proxychains.conf")
		os.system("sudo tor")
	if Choose==("3"):
		os.system("nano /etc/proxychains.conf")
	else:
		print("Syntax Error ")
code_bn()
    
