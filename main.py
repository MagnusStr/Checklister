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
                f.write("https://github.com/MagnusStr/tests-n-drafts/archive/refs/heads/main.zip")

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
        os.mkdir("Programas")
        os.chdir(".\Programas")
        for url in lines:
            wget.download(url)
            time.sleep(2)
        
        n_path = os.getcwd()
        #Instalar Programas
        for a in n_path:
            


web = Webmodule()
files = Storage()        
if(files.checar_links() == False):
    files.criar_lista()


print("Baixando programas\n")
web.download_apps() 
if (web.checar_winget() == True):
    print("Winget instalado na máquina!\n")
    

else:
    print("Winget não instalado na máquina\n")
    print("Baixando winget!\n")
   
