# Lê o valor total da compra como inteiro
valor_compra = int(input())

# Verifica qual benefício deve ser aplicado
if valor_compra < 50:
    print("Obrigado por comprar conosco!")
elif valor_compra <= 99:
    print("Parabens! Voce ganhou um brinde!")
elif valor_compra <= 199:
    print("Desconto de 10 reais aplicado!")
else:
    print("Desconto de 25 reais aplicado!")