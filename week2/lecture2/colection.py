class Pessoa:
    def __init__ (self, nome, nota):
        self.nome = nome
        self.nota = nota


pessoa1 = Pessoa("Vitor", 727)
pessoa2 = Pessoa("Pedro", 744)
pessoa3 = Pessoa("Joana", 543)

pessoas = [pessoa1, pessoa2, pessoa3]

lista_aprovados = []

for pessoa in pessoas:
    if pessoa.nota > 600:
        lista_aprovados.append(pessoa)

for pessoa in lista_aprovados:
    print(f"Nome: {pessoa.nome}, Nota: {pessoa.nota}")