# Lê o valor da transação, a taxa de serviço e o pagamento mínimo
valor, taxa, minimo = map(int,input().split())

# Calcula o valor final da transação
valor_final = valor - taxa

# Verifica se a transação pode ser aprovada
if valor_final >= minimo:
    print("Aprovada")
else:
    print("Recusada")