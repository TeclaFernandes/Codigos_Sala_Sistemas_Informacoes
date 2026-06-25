def padronizar_nome(nome):
    # Inicializa uma string para armazenar o nome padronizado
    nome_padronizado = ''
    
    # Define uma variável que indica se a próxima letra deve ser maiúscula
    maiusculo = True
    
    # Percorre cada caractere da string fornecida
    for caractere in nome:
        # Obtém o valor ASCII do caractere atual
        ascii_val = ord(caractere)
        
        # Verifica se o caractere é uma letra minúscula ('a' a 'z')
        if 'a' <= caractere <= 'z':
            if maiusculo:
                # Converte a letra minúscula para maiúscula ajustando o valor ASCII
                nome_padronizado += chr(ascii_val - 32)
                # Define que o próximo caractere não deve ser maiúsculo
                maiusculo = False
            else:
                # Mantém a letra minúscula como está
                nome_padronizado += caractere
        
        # Verifica se o caractere é uma letra maiúscula ('A' a 'Z')
        elif 'A' <= caractere <= 'Z':
            if not maiusculo:
                # Converte a letra maiúscula para minúscula ajustando o valor ASCII
                nome_padronizado += chr(ascii_val + 32)
            else:
                # Mantém a letra maiúscula como está
                nome_padronizado += caractere
            # Define que o próximo caractere não deve ser maiúsculo
            maiusculo = False
        
        # Verifica se o caractere é um espaço ou outro caractere não alfabético
        else:
            # Adiciona o caractere ao resultado sem alterações
            nome_padronizado += caractere
            # Define que o próximo caractere deve ser maiúsculo se o caractere atual for um espaço
            if caractere == ' ':
                maiusculo = True
    
    # Retorna a string com a capitalização ajustada
    return nome_padronizado

# Solicita ao usuário o número de clientes
n = int(input("Digite o número de clientes: "))

# Lê e padroniza o nome de cada cliente
for _ in range(n):
    # Recebe o nome do cliente da entrada padrão
    nome_cliente = input("Digite o nome do cliente: ")
    # Aplica a função de padronização ao nome do cliente
    nome_padronizado = padronizar_nome(nome_cliente)
    # Exibe o nome padronizado
    print(f"Nome padronizado: {nome_padronizado}")
