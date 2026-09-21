# Classe que representa um cliente
class Cliente:
    def __init__(self, nome, email, saldo):
        self.nome = nome
        self.email = email
        self.saldo = saldo

# Leitura dos dados do cliente 
nome = input()
email = input()
saldo = int(input())

# Criação do objeto Cliente
cliente = Cliente(nome, email, saldo)

# Verifica se o cliente é VIP
if cliente.saldo >= 1000:
    print("VIP")

else:
    print("REGULAR")