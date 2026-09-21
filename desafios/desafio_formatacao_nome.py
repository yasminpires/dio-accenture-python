# Lê o nome do cliente
nome = input()

# Remove espaços entre extras e ajusta a capitalização
nome_formatado = nome.strip().split()
nome_formatado = " ".join(nome_formatado).title()

# Exibe o nome formatado
print(nome_formatado)