import os
import wget

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
        print("Baixando os programas...\n")
        with open("database.txt") as f:
            lines = f.readlines()
            for url in lines:
                wget.download(url)

