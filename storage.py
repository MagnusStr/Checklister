import os
class Storage:  

    global x
    x = 0
    #checar se existe txt
    def checar_links(self):
        diretorio = os.getcwd()
        listar = os.listdir(diretorio)
        arq = "database.txt"
        for i in listar:  
            if i == arq:
                x = 1
                
            else:
                x = 0
  
        
    #criar txt
    def criar_lista(self):
        if x == 0:
            with open('database.txt', 'w') as f:
                f.write("")
            
        else:
            pass

#    def inserir_links(self,link):
#        with open('database.txt',w)  as d:
#            d.write(link)      
            
    
    