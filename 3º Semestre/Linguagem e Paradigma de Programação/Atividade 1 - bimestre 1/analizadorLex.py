class AnalizadorLexico:

    # define att. principais
    def __init__(self, entrada):
        self.entrada = iter(entrada)
        self.charAtual = None
        self.classeChar = None

        self.proximoChar()

    # Busca próximo caractere
    def proximoChar(self):

        self.charAtual = None
        try:
            proximoChar = next(self.entrada)
            self.charAtual = proximoChar
            self.getChar()
            
        except StopIteration:
            self.charAtual = None

    # Verifica/atualiza a classe do caractere atual
    def getChar(self):
        
        self.classeChar = None
        if self.charAtual != None:
            if self.charAtual.isalpha():
                self.classeChar = "LETRA"

            elif self.charAtual.isdigit():
                self.classeChar = "DIGITO"

            else:
                self.classeChar = "DESCONHECIDO"

    # Vai passar por todos os espaços vazios
    def getNaoVazio(self):
        while self.charAtual is not None and self.charAtual.isspace():
            self.proximoChar()
            
    # Método principal
    def lex(self):
        
        lexema = ""
        self.getNaoVazio()

        # Acaba quando caractere atual não existir mais
        if self.charAtual == None:
            return ["EOF", "EOF"]
        
        # Verificação para lexema ID
        if self.classeChar == "LETRA":
            lexema += self.charAtual
            self.proximoChar()

            while self.charAtual is not None and self.classeChar in ("LETRA", "DIGITO"):
                lexema += self.charAtual
                self.proximoChar()

            return [lexema, "ID"]
        
        # Verificação para INT
        if self.classeChar == "DIGITO":
            lexema += self.charAtual
            self.proximoChar()

            while self.classeChar == "DIGITO" and self.charAtual is not None:
                lexema += self.charAtual
                self.proximoChar()
            
            return [lexema, "INT"]
        
        # Verificação em caso de tokens
        if self.classeChar == "DESCONHECIDO":

            if self.charAtual == "*":
                self.proximoChar()

                if self.charAtual == "*":
                    self.proximoChar()
                    return ["**", "OPEXP"]
                
                return ["*", "OPMULTIPLICACAO"]
                
            lexema = self.charAtual
            token = self.verificaToken()
            self.proximoChar()
            return [lexema, token]
    
    # VERIFICA TOKENS
    def verificaToken(self):
        tokens = {
                "+": "OPSOMA",
                "-": "OPSUBTRACAO",
                "/": "OPDIVISAO",
                "%": "OPMODULO",
                "=": "OPATRIBUICAO",
                "(": "ABRE_PAREN",
                ")": "FECHA_PAREN",
                ";": "PONTO_VIRG"}
        
        return tokens.get(self.charAtual)
