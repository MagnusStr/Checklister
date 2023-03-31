from tkinter import *

class Interface:
    def __init__(self):
        #começo
        self.janela = Tk()
        #configurações de janela
        self.janela.minsize(width=650, height=750)
        self.janela.geometry("650x750")
        self.janela.resizable(0,0)
        #aplicação
        self.label = Label(self.janela, text="Teste")
        self.label.pack()
        #final
        self.janela.mainloop()
        
        
teste = Interface()
teste.janela()
