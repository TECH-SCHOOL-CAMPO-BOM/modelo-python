# Aula 12 - Exemplo 1
# Classe com __init__

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


pessoa1 = Pessoa("Ana", 17, "Campo Bom")

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.cidade)
