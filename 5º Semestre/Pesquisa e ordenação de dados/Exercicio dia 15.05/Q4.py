# Cadastro de Pessoas em Sistema de Saúde

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return self.nome == other.nome and self.idade == other.idade
        return False

    def __hash__(self):
        return hash((self.nome, self.idade))

p1 = Pessoa("Ana", 25)
p2 = Pessoa("Ana", 25)
p3 = Pessoa("Pedro", 30)

prontuario = {}
prontuario[p1] = "Diabetes tipo 2"
prontuario[p3] = "Cirrose"

print(prontuario[p2]) 
print(len(prontuario))  