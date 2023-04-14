import time
import os
import wget

class Storage:  
    #checar se existe txt
    def checar_links(self):
        diretorio = os.getcwd()
        listar = os.listdir(diretorio)
        arq = "database.txt"
        for i in listar:  
            if i == arq:
                return True
            else:
                return False

    #criar txt
    def criar_lista(self):
            with open('database.txt', 'w') as f:
                f.write("")

class Webmodule:             

    def checar_winget(self):
        dir = "C:\\Program Files\\WindowsApps\\"
        winget = "Microsoft.DesktopAppInstaller_1.19.10173.0_x64__8wekyb3d8bbwe"
        list = os.listdir(dir)
        for i in list:
            if(i == winget):
                return True
            else:
                return False


    def download_apps(self):
        with open("database.txt", 'r') as f:
            lines = f.readlines()
        os.mkdir("Downloads")
        os.chdir(".\Downloads")
        for url in lines:
            wget.download(url)
            time.sleep(3)
        arq_p = os.listdir()
        for m in arq_p:
            os.system("start /wait {}".format(m))

web = Webmodule()
files = Storage()        
if(files.checar_links() == False):
    files.criar_lista()

print("Baixando programas...\n")
web.download_apps()
os.system("winget upgrade --all")
   
