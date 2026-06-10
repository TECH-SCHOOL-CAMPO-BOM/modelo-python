# Aula 12 - Exemplo 2
# Classe com método

class Pessoa:
  def __init__ (self, nome, idade, cidade):
    self.nome = nome
    self.idade = idade
    self.cidade = cidade

  def apresentar (self):
    print(f"{self.nome} tem {self.idade} anos e mora em {self.cidade}.")

pessoa1 = Pessoa("Ana", 17, "Campo Bom")
pessoa1.apresentar()
