import os
import requests
import wget

class Webmodule:             
   
    def checar_conexao(self):
        try:
            requests.get('https://www.google.com', timeout=5)
            return True
            print("Essa máquina possui conexão com a internet!")
        except exceptions.ConnectionError:
            return False
            print("Essa máquina não possui conexão com a internet!")
    
    def checar_winget(self):
        dir = "C:\\Program Files\\WindowsApps\\"
        winget = "Microsoft.DesktopAppInstaller_1.19.10173.0_x64__8wekyb3d8bbwe"
        list = os.listdir(dir)
        for i in list:
            if(i == winget):
                print("Winget instalado na máquina!")


    def download_apps(self):
        with open(".\database.txt") as f:
            lines = f.readlines()
            for url in lines:
                wget.download(url)
       
                
teste = Webmodule()
teste.checar_conexao()
teste.checar_winget()
teste.download_apps()