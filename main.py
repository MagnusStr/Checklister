import time
import subprocess
import selenium
from webmodule import Webmodule

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#PARA SISTEMAS LINUX: from webdriver_manager.chrome import ChromeDriverManager

#Adobe
#Zips
#PDF
#Navegadores
#Office
#Anydesk
#UltraVNC

# links = ['https://get.adobe.com/br/reader/download?os=Windows+11&name=Reader+DC+2023.001.20064+Brazilian+Windows%2864Bit%29&lang=br&nativeOs=Linux+x86_64&accepted=&declined=&preInstalled=&site=otherversions',
# 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe',
# 'https://7-zip.org/a/7z2201-x64.exe',
# 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247917_0ae14417abb444ebb02b9815e2103550',
# 'https://uvnc.com/component/jdownloads/send/0-/438-ultravnc-1409-x64-setup.html?Itemid=0',
# 'https://anydesk.com/pt/downloads/windows?dv=win_exe',
# 'https://github.com/microsoft/winget-cli/releases/download/v1.4.10173/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle',
# 'https://www.mozilla.org/pt-BR/firefox/download/thanks/']

web = Webmodule()
        
if (web.checar_conexao() == True):
    print('alo')
    
else:
    print("Não foi identificado conexão com a internet. Cheque sua conexão!")   

