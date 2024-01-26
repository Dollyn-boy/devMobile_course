class Tripulante:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def executar_tarefa(self):
        pass    

    @classmethod        #método de classe, 
    def criar_tripulante(cls, nome, idade): # cls é o próprio objeto da classe
        return cls(nome, idade)

class Piloto(Tripulante):

    def executar_tarefa(self):

        print(f"{self.nome} está pilotando a nave...")

class Engenheiro(Tripulante):

    def executar_tarefa(self):
        print(f"{self.nome} está reparando a nave...")

class Navegador(Tripulante):

    def executar_tarefa(self):
        print(f"{self.nome} está verificando mapa galáctico...")

tripulante1 = Piloto.criar_tripulante("Joana", "17")
tripulante2 = Engenheiro.criar_tripulante("Heithor", "17")
tripulante3 = Navegador.criar_tripulante("Amanda", "19")

tripulantes = [tripulante1, tripulante2, tripulante3]

for tripulante in tripulantes:
    tripulante.executar_tarefa()