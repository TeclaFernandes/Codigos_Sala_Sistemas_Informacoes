def extrair_dominio(url):
    # Inicializa a posição dos prefixos e prefixo www.
    pos_https = 0
    pos_http = 0
    pos_www = 0

    # Verifica se a URL começa com 'https://'
    # Se a URL tiver pelo menos 8 caracteres e os primeiros 8 caracteres forem 'https://'
    if len(url) >= 8 and url[:8] == 'https://':
        pos_https = 8  # Define a posição de onde o domínio começa após 'https://'
    
    # Verifica se a URL começa com 'http://'
    # Se a URL tiver pelo menos 7 caracteres e os primeiros 7 caracteres forem 'http://'
    elif len(url) >= 7 and url[:7] == 'http://':
        pos_http = 7  # Define a posição de onde o domínio começa após 'http://'
    
    # Remove o prefixo 'https://' ou 'http://', se encontrado
    # Ajusta a URL para começar logo após o prefixo encontrado
    if pos_https > 0:
        url = url[pos_https:]
    elif pos_http > 0:
        url = url[pos_http:]
    
    # Remove o prefixo 'www.' se presente
    # Se a URL tiver pelo menos 4 caracteres e os primeiros 4 caracteres forem 'www.'
    if len(url) >= 4 and url[:4] == 'www.':
        pos_www = 4  # Define a posição de onde o domínio começa após 'www.'
    
    if pos_www > 0:
        url = url[pos_www:]  # Ajusta a URL para começar logo após o prefixo 'www.'
    
    # Remove o caminho final e parâmetros, se houver
    pos = len(url)  # Inicialmente, define a posição como o comprimento total da URL
    
    # Percorre cada caractere da URL para encontrar o início do caminho ou parâmetros
    for i in range(len(url)):
        # Se encontrar um caractere '/', '?' ou '#', ajusta a posição
        if url[i] in ['/', '?', '#']:
            pos = i
            break  # Sai do loop assim que encontra um caractere que indica o início do caminho ou parâmetros
    
    # Pega a parte da URL que corresponde ao domínio, até a posição encontrada
    dominio = url[:pos]
    
    return dominio  # Retorna o domínio extraído

# Exemplo de uso
url1 = "https://www.ifce.edu.br/"  # URL de exemplo
dominio = extrair_dominio(url1)  # Chama a função para extrair o domínio
print(f"Domínio extraído: {dominio}")  # Exibe o domínio extraído
url2 = "https://sdeskce.jodibe.com.br/admin/admin_main.php"  # URL de exemplo
dominio = extrair_dominio(url2)  # Chama a função para extrair o domínio
print(f"Domínio extraído: {dominio}")  # Exibe o domínio extraído
url3 = "http://gjd.promaxcloud.com.br/pw"  # URL de exemplo
dominio = extrair_dominio(url3)  # Chama a função para extrair o domínio
print(f"Domínio extraído: {dominio}")  # Exibe o domínio extraído
