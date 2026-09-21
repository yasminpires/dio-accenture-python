# Função para validar o e-mail
def validar_email(email):
    # O e-mail deve ter exatamente um @
    if email.count("@") != 1:
        return False

    # Localiza a posição do @
    posicao_arroba = email.index("@")

    # Verifica se existe um ponto depois do @
    if "." not in email[posicao_arroba + 1:]:
        return False

    return True

# Função para formatar o nome 
def formatar_nome(nome):
    palavras = nome.strip().split()
    palavras_formatadas = [palavra.capitalize() for palavra in palavras]

    return " ".join(palavras_formatadas)

# Lê o nome e o e-mail
entrada = input()

# Separa o nome do e-mail
nome, email = entrada.split(", ")

# Formata o nome 
nome_formatado = formatar_nome(nome)

# Verifica o e-mail e define o resultado
if validar_email(email):
    print(nome_formatado + " - OK")

else:
    print(nome_formatado + " - ERRO")