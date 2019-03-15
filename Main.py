import os
import sys
import socket as sk
from colorama import Style,Fore,Back


class HaxRus():
	def cs_x():
		print(Back.WHITE+Fore.BLACK+"WARNING"+Fore.RESET+Back.RESET)
		os.system("echo Do not forget to enter input as requested")
		sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
		print(Fore.RED+"checking Root!!"+Fore.RESET)
		yes=("Y" or "y" or "yes" or "Yes")
		no=("N" or "n" or "no" or "No")
		dake=(input(Fore.RED+"Do you Have root? Type Y or N :  "+Fore.RESET))
		if dake!=((yes)):
			os.system("killall *")
		main_1=(Fore.BLUE+"1.Start Tor")
		main_2=("2.Start DDOS Botnet")
		main_3=("3.Edit Proxychains/Tor file(requires root)")
		main_4=("0.Exit Hax4Us"+Fore.RESET)
		os.system("figlet 100% loaded")
		os.system("toilet -F metal HaxRuS")
		print (main_1)
		print (main_2)
		print (main_3)
		print (main_4)
		Choose=input(Fore.BLUE+"choose your option:"+Fore.RESET)
		if Choose==("1"):
			toron=(input(Fore.CYAN+"You MUST be ONLINE! If you're not...Type (N),If you are...type (Y) :   "+Fore.RESET))
			if toron==((yes)):
				print (Fore.GREEN+"Tor loading now"+Fore.RESET)
				os.system("tor")
			elif toron==((no)):
				print (Fore.RED+"Tor is Unable to work offline"+Fore.RESET)
				os.system("killall tor")
			else:
				print("Invalid Option! If tor isnt responding Contact Us on github")
		if Choose==("3"):
			os.system("nano /etc/proxychains.conf")
		if Choose==("2"):
			os.system("python Main_bn.py")
		if Choose==("4"):
			print ("loading hidden option!!")
			input_vpnh=(input(Fore.YELLOW+"Do you know how to use OPENVPN? :  "))
			if input_vpnh==(yes):
				command_one=input("What command Extension do you want to use?"+Fore.RESET) 
				os.system("sudo openvpn "+(command_one))
			if input_vpnh==(no):
				print("Help from OPENVPN")
				os.system("openvpn -help")
		if Choose==("0"):
			os._exit(0)
		elif dake==((no)):
			print("Syntax Error...Please Try again later")
			os.system("fakeroot")
			print("Try again...Weve faked your ROOT permissions!")
			os._exit(0)
		else:
			print("Wrong Answer!!!")
	cs_x()

HaxRus()
