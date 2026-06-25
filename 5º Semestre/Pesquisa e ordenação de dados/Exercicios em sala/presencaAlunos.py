alunos = ["Tecla", "Gustavo", "Lucas", "Fernando", "Tecla", "Diego", "Horstman", "Horstman", "Tecla"]

def chave_valor(alunos):
    resultado = {}

    for i, nome in enumerate(alunos):
        if nome not in resultado:
            resultado[nome] = []
        resultado[nome].append(i)

    return resultado

result = chave_valor(alunos)
print(result)