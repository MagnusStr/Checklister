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
            #botão add/remove
        self.add_btn = Button(self.janela, text="Adicionar Link",command=) #,command=
        self.add_btn.pack()
        self.rem_btn = Button(self.janela, text="Remover Link") #,command=
        self.rem_btn.pack()
        self.entrada = Entry(self.janela, width=100)
        self.entrada.pack()
        #final
        self.janela.mainloop()
        
        
teste = Interface()
teste.janela()
