from tkinter import *
from tarefa import Tarefa

class App:
    def __init__(self,titulo="Minhas Tarefas"):
        self.tela = Tk()
        self.tela.title(titulo)
        self.tela.geometry("250x500")
        
        self.lb_titulo = Label(self.tela, text="Minhas Tarefas", font="Arial 12 bold", fg="red")
        self.lb_titulo.pack()

        self.btnAdd = Button(self.tela, text="ADD", width=20, bg="green", fg="white", command=self.addTarefa)
        self.btnAdd.pack()

        self.btnEdit = Button(self.tela, text="EDIT", width=20, bg="green", fg="white", state=DISABLED, command=self.editTarefa)
        self.btnEdit.pack()

        self.btnDel = Button(self.tela, text="DEL", width=20, bg="green", fg="white", state=DISABLED, command=self.Apagar)
        self.btnDel.pack()

        self.btnCheck = Button(self.tela, text="CHECK", width=20, bg="green", fg="white", state=DISABLED, command=self.Concluir)
        self.btnCheck.pack()

        self.scroll = Scrollbar(self.tela)
        self.scroll.pack(side=RIGHT, fill= Y)

        self.lista = Listbox(self.tela, yscrollcommand=self.scroll.set, height=500)
        self.tarefas = []

        self.selection = None

        self.montar_tarefas()

    def montar_tarefas(self):
        self.lista.delete(0,END)
        for t in self.tarefas:
            if t.concluido:
                self.lista.insert(END, t.tarefa+" - concluido")
            else:
                self.lista.insert(END, t.tarefa)
        self.lista.pack(fill= BOTH)
        self.scroll.config(command=self.lista.yview)
        self.lista.bind("<<ListboxSelect>>",self.SelectItem)

    def SelectItem(self,event):
        selection = event.widget.curselection()
        if selection:
            self.selection = selection[0]
            self.btnEdit.config(state=NORMAL)
            self.btnDel.config(state=NORMAL)
            self.btnCheck.config(state=NORMAL)

    def addTarefa(self):
        self.selection = None
        self.addtela = Tk()

        self.lb_tt = Label(self.addtela, text="Adicionar Tarefas",font="Arial 15 bold",fg="gray")
        self.lb_tt.pack()

        self.entrada = Text(self.addtela,height=20)
        self.entrada.pack()

        self.btnAdd100= Button(self.addtela, text="teste! (Adicionar 100)", bg="green", fg="white", command=self.add100)
        self.btnAdd100.pack()

        self.btnSalvar = Button(self.addtela, text="Salvar", bg="green", width=10, fg="white", command=self.Salvar)
        self.btnSalvar.pack()

        self.addtela.mainloop()

    def editTarefa(self):
        self.addtela = Tk()

        self.lb_tt = Label(self.addtela, text="Editar Tarefas",font="Arial 15 bold",fg="gray")
        self.lb_tt.pack()

        self.entrada = Text(self.addtela,height=20)
        self.entrada.pack()
        if self.selection != None:
            self.entrada.insert('1.0',self.tarefas[self.selection].tarefa)

        self.btnSalvar = Button(self.addtela, text="Salvar", bg="green", width=10, fg="white", command=self.Salvar)
        self.btnSalvar.pack()

        self.addtela.mainloop()
    
    def Salvar(self):
        if self.selection != None:
            self.tarefas[self.selection].tarefa = self.entrada.get("1.0",'end-1c')
            self.selection = None
        else:
            self.tarefas.append(Tarefa(self.entrada.get("1.0",'end-1c')))
        self.addtela.destroy()
        self.montar_tarefas()

    def Apagar(self):
        if self.selection != None:
            self.tarefas.pop(self.selection)
            self.selection = None
        self.montar_tarefas()

    def Concluir(self):
        if self.selection != None:
            self.tarefas[self.selection].Concluir()
            self.selection = None
        self.montar_tarefas()

    #desafio extra
    def add100(self):
        self.addtela.destroy()
        for i in range(100):
            self.tarefas.append(Tarefa("Tarefa nº: "+str(i+1)))
        self.montar_tarefas()

    def run(self):
        self.tela.mainloop()