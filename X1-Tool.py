import os 
import time
print(" we want to update system please tap  Y  to continue or  n  to exit ")
h=input("please Enter Y or n : ")
if ("h==n"):
	pass
elif ("h==y"):
	os.system("apt update -y")
	os.system("apt upgrade -y")
time.sleep(3)
os.system ("clear")
def menu():
	print("")

print("""
          '||' '|'      ' |''||''|                 '||         
            || |    /|       ||      ...     ...    ||   ....  
             ||    /||       ||    .|  '|. .|  '|.  ||  ||. '  
            | ||    ||       ||    ||   || ||   ||  ||  . '|.. 
          .|   ||.  ||      .||.    '|..|'  '|..|' .||. |'..|' 
               ||                                         
                   ,/-'  

- - - - - - - - -  - - - - -  - --  - -  -  - -  - - - - - -  - - - -  - - - - - - - --  - - - -  - - - --  --
- - - - - - - -  - -  - -   - - -- - - - - - - - - -  -- - -- --  --  - - - - - - - - - -- - - - -- - - - - --



_______________________________________
Created        By        Wihacker_X1 
______________________________________


tihs tool for Ethical Hacking  

____________________________________________________

              enjoy  with Tools
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _  _ _ _ _ _ _  _

1: install SQLmap 
_________________________________________
2: install Facebook-Brutforce
_________________________________________
3: install smsbombing 
_________________________________________
4: install routeursploit
_________________________________________
5: install wifite   
_________________________________________
6: install kali-nethunter-termux
_________________________________________
7: install nmap 
_________________________________________
8: install PAYGEN
_________________________________________
9: install UndetectedPythonPayload
_________________________________________
10: install VIsql
_________________________________________
11: install jarbou3
-----------------------------------------
00: To Exit
-----------------------------------------
-----------------------------------------
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "1":
    		os.system("apt update -y")
    		os.system("cd $HOME")
    		os.system("git clone https://github.com/sqlmapproject/sqlmap.git")
    		print("                        Do YOU WANT TO CONTINUE")
    		rmenu = input("[?] Back to Menu? (y/n): ")
    		if rmenu == "y":
    			menu()
    		else:
    			break
    elif what== "2":
    		os.systeme("git clone https://github.com/youhacker55/FB-CRACKER")
    elif what=="3":
    		os.system("git clone https://github.com/youhacker55/smsbombing")
    		print("decrypt the programe for password with Base64")
    		menu()
    elif what=="4":
    		os.system("git clone https://github.com/reverse-shell/routersploit.git")
    		print("routersploit installed successfully ;) ")
    		menu()
    elif what=="5":
    		os.system("git clone  https://github.com/derv82/wifite")
    		print ("wifite installed successfully ;)")
    		menu()
    elif what=="6":
    		os.system("clear")
    		print("nethunter will take some time please wait")
    		os.system("cd /data/data/com.termux/files/home && pkg install wget && wget -O install-nethunter-termux https://offs.ec/2MceZWr")
    		os.system("clear")
    		print("this will take some time") 
    		os.system("cd /data/data/com.termux/files/home && chmod +x install-nethunter-termux")
    		os.system("cd /data/data/com.termux/files/home && ./install-nethunter-termux")
    		os.system("clear")
    		print("kali-nethunter installed successfully run it with ' nh ' ;)  ")
    		menu()
    		
    elif what=="7":
    		os.system("clear")
    		z=input( "if you are use termux enter t or enter K for kali :   ")
    		if z==t:
    			os.system("pkg install nmap")
    		elif z==K:
    			os.system("sudo apt-get install namp")
    		else:
    			print("		ERROR PLEASE ENTER t  OR K	")
    elif what=="8":
    		os.system("clear")
    		os.system("git clone https://github.com/youhacker55/PayGen")
    elif what=="11":
    		os.system("git clone https://github.com/youhacker55/jarbou3")
    elif what=="9":
    		os.system("git clone https://github.com/youhacker55/UndetectedPythonPayload")
    elif what=="11":
    		os.system("git clone https://github.com/paulfitz/visql")


#thanks for use my tool :)
