import time
import os
import wget
import requests
from storage import Storage
from webmodule import Webmodule

web = Webmodule()
files = Storage()        
if (web.checar_conexao() == True):
    files.checar_links()
    files.criar_lista()
    web.download_apps()
    web.checar_winget()
else:
    print("Não foi identificado conexão com a internet. Cheque sua conexão!")   

