import time
import os
import wget
from storage import Storage
from webmodule import Webmodule

web = Webmodule()
files = Storage()        
files.checar_links()
files.criar_lista()
web.download_apps()
web.checar_winget() 

