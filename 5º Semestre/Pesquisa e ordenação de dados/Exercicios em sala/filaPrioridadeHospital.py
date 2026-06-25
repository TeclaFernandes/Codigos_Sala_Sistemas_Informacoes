class Paciente:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def __repr__(self):
        return f"{self.nome} (Prioridade {self.prioridade})"


def chamar_paciente(fila):
    if not fila:
        return None

    indice_maior = 0

    for i in range(1, len(fila)):
        if fila[i].prioridade > fila[indice_maior].prioridade:
            indice_maior = i

    return fila.pop(indice_maior)

fila = [
    Paciente("Ana", 2),
    Paciente("Carlos", 5),
    Paciente("João", 3),
    Paciente("Maria", 5),
    Paciente("Pedro", 1)
]

paciente = chamar_paciente(fila)
print("Paciente da vez", paciente)