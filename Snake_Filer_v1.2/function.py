import requests

def search_file(os_type,file_type_windows,file_type_linux):
    if os_type == "w" or os_type == "W":
        for i,windows in enumerate(file_type_windows):
            print(f"{i}. {windows}")
        n = int(input("Choose the name of the file you want:  "))
        p = file_type_windows[n]
        return p
        
    if os_type =="l" or os_type == "L":
        for i,linux in enumerate(file_type_linux):
            print(f"{i}. {linux}")
        n = int(input("Choose the name of the file you want:  "))
        p = str(file_type_linux[n])
        return p
    


def file_linux():
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
    "var/lib/mlocate.db"]
    return file_type_linux

def file_windows():
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
    "c:/windows/system.ini"]
    return file_type_windows