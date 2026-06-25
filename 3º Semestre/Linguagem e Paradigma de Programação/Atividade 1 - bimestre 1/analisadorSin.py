import analizadorLex as al

class AnalisadorSintatico:
    def __init__(self, lexico):
        self.lexico = lexico
        self.token = None
        self.valor = None
        self.proximo()

    def proximo(self):
        self.valor, self.token = self.lexico.lex()

    def erro(self, esperado):
        raise SyntaxError(f"Erro de sintaxe: esperava {esperado}, mas encontrou '{self.valor}' ({self.token})")

    def verifica_token(self, esperado_token):
        if self.token == esperado_token:
            self.proximo()
        else:
            self.erro(esperado_token)

    # expr → termo { ( + | - ) termo }
    def expr(self):
        self.termo()
        while self.token in ("OPSOMA", "OPSUBTRACAO"):
            self.proximo()
            self.termo()

    # termo → fator { ( * | / | % ) fator }
    def termo(self):
        self.fator()
        while self.token in ("OPMULTIPLICACAO", "OPDIVISAO", "OPMODULO", "OPEXP"):
            self.proximo()
            self.fator()

    # fator → INT | ID | ( expr )
    def fator(self):
        if self.token in ("INT", "ID"):
            self.proximo()
        elif self.token == "ABRE_PAREN":
            self.proximo()
            self.expr()
            self.verifica_token("FECHA_PAREN")
        else:
            self.erro("INT, ID ou '('")

    # Function principal
    def analisador(self):
        self.expr()
        if self.token != "EOF":
            self.erro("fim da expressão")

entrada = "a + 1 ** 3 - (4 * 20)"
lexico = al.AnalizadorLexico(entrada)
sintatico = AnalisadorSintatico(lexico)

try:
    sintatico.analisador()
    print("Expressão válida!")
except SyntaxError as e:
    print(e)
