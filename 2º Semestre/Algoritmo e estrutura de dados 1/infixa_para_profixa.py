# Função que retorna a precedência dos operadores
def precedencia(op):
    if op == '^':  # Exponenciação tem a maior precedência
        return 3
    if op in ('*', '/'):  # Multiplicação e divisão vêm a seguir
        return 2
    if op in ('+', '-'):  # Soma e subtração têm a menor precedência entre os operadores
        return 1
    return 0  # Qualquer outro caractere tem precedência 0 (não operador)


# Função para converter expressão infixa para pós-fixa
def infixa_para_posfixa(expressao):
    saida = ""  # Armazena a expressão pós-fixa resultante
    pilha = []  # Pilha para armazenar operadores temporariamente

    # Percorre cada caractere da expressão de entrada
    for char in expressao:
        if char.isalnum():  # Se for um operando (letra A-Z ou número 0-9), adiciona diretamente à saída
            saida += char
        elif char == '(':  # Se for um parêntese de abertura, empilha
            pilha.append(char)
        elif char == ')':  # Se for um parêntese de fechamento
            while pilha and pilha[-1] != '(':  # Desempilha tudo até encontrar um '('
                saida += pilha.pop()  # Adiciona operadores à saída
            pilha.pop()  # Remove o '(' da pilha (não vai para a saída)
        else:  # Se for um operador (+, -, *, /, ^)
            # Desempilha operadores de maior ou igual precedência antes de empilhar o novo operador
            while (pilha and pilha[-1] != '(' and
                   (precedencia(pilha[-1]) > precedencia(char) or
                    (precedencia(pilha[-1]) == precedencia(char) and char != '^'))):  
                saida += pilha.pop()  # Move o operador da pilha para a saída
            pilha.append(char)  # Empilha o operador atual

    # Após percorrer toda a expressão, desempilha operadores restantes
    while pilha:
        saida += pilha.pop()

    return saida  # Retorna a expressão na forma pós-fixa
