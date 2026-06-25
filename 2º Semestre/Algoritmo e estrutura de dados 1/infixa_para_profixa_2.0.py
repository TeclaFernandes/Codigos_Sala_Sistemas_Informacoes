class No:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
 
class Pilha:
    def __init__(self):
        self.primeiro = None
 
    def vazia(self):
        return self.primeiro is None
 
    def push(self, valor):
        novo = No(valor)
        novo.prox = self.primeiro
        self.primeiro = novo
 
    def pop(self):
        if self.vazia():
            return None
        v = self.primeiro.info
        self.primeiro = self.primeiro.prox
        return v
 
    def topo(self):
       
     if self.vazia():
         return None
     else:
         return self.primeiro.info
 
def precedencia(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0
 
def infixa_para_posfixa(expressao):
    saida = ""
    pilha = Pilha()
 
    for char in expressao:
        if char.isalnum():
            saida += char
 
        elif char == '(':
            pilha.push(char)
 
        elif char == ')':
            while pilha.topo() != '(':
                saida += pilha.pop()
            pilha.pop()
 
        else:
            while (not pilha.vazia() and (precedencia(pilha.topo()) >= precedencia(char))):
                saida += pilha.pop()
            pilha.push(char)
 
    while not pilha.vazia():
        saida += pilha.pop()
 
    return saida
 
n = int(input())
for i in range(n):
    entrada = input()
    print(infixa_para_posfixa(entrada))