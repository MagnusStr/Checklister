import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import glob
from tqdm import tqdm

#Adobe
#Zips
#PDF
#Navegadores
#Office
#Anydesk
#UltraVNC

links = ['https://get.adobe.com/br/reader/download?os=Windows+11&name=Reader+DC+2023.001.20064+Brazilian+Windows%2864Bit%29&lang=br&nativeOs=Linux+x86_64&accepted=&declined=&preInstalled=&site=otherversions',
'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe','https://7-zip.org/a/7z2201-x64.exe','https://javadl.oracle.com/webapps/download/AutoDL?BundleId=247917_0ae14417abb444ebb02b9815e2103550','https://uvnc.com/component/jdownloads/send/0-/438-ultravnc-1409-x64-setup.html?Itemid=0','https://anydesk.com/pt/downloads/windows?dv=win_exe']
#Navegador
navegador = webdriver.Chrome(ChromeDriverManager().install())
#Configurações
navegador.maximize_window()

def baixar_programas(link):
    for i in tqdm(range(1)):
        time.sleep(8)
        #Adobe
        navegador.get(links[0])
        time.sleep(8)
        #7ZIP
        navegador.get(links[1])
        time.sleep(8)
        #Java
        navegador.get(links[2])
        time.sleep(8)
        #UltraVNC
        navegador.get(links[3])
        time.sleep(8)
        #Anydesk
        navegador.get(links[4])
        time.sleep(8)
        #
        navegador.get(links[5])
        time.sleep(8)


def instalar_office():
    pass


baixar_programas(links)
checar()



