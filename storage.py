import os
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


#    def inserir_links(self,link):
#        with open('database.txt',w)  as d:
#            d.write(link)      
            
    
    