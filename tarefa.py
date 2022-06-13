class Tarefa:
    tarefa = ""
    concluido = False
    def __init__(self, tarefa, concluido=False):
        self.tarefa = tarefa
        self.concluido = concluido
    
    def Concluir(self):
        self.concluido = True

    def __str__(self):
        if self.concluido:
            return "Tarefa: "+self.tarefa+" estado: concluido"
        else:
            return "Tarefa: "+self.tarefa+" estado: em espera"