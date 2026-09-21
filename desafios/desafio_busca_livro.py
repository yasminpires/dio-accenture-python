# Leitura da quantidade de livros cadastrados
n = int(input())

# Dicionário para armazenar o acervo: título -> código
acervo = {}

# Leitura dos pares título-código
for _ in range(n):
    linha = input().strip()

    # Separa o título e o código
    titulo, codigo = linha.split()

    # Adiciona o livro ao dicionário
    acervo[titulo] = codigo

# Leitura do título a ser consultado
consulta = input().strip()

# Busca pelo título no acervo e impressão do resultado
if consulta in acervo:
    print(acervo[consulta])
else:
    print("Livro nao encontrado")