import os
import sys
import socket as sk
from colorama import Style,Fore,Back


class DDOS():

	def code_bn():
		main_1=(Fore.BLUE+"1.Start Tor")
		main_2=("2.Start DDOS Botnet")
		main_3=("3.Edit Proxychains/Tor file(requires root)")
		main_4=("0.Exit Hax4Us"+Fore.RESET)
		os.system("figlet 100% loaded")
		os.system("toilet -F metal HAX4US")
		print (main_1)
		print (main_2)
		print (main_3)
		print (main_4)
		Choose=input(Fore.BLUE+"choose your option:"+Fore.RESET)
		if Choose==("1"):
			os.system("tor")
		if Choose==("3"):
			os.system("nano /etc/proxychains.conf")
		if Choose==("2"):
			os.system("python Main_bn.py")
		else:
			print("Syntax Error...Please Try again later")
	code_bn()
DDOS()   
    
