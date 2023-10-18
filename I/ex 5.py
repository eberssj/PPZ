mercadoria = float(input("Preço da mercadoria:"))
desconto = float(input("Percentual de desconto:"))
des = mercadoria * desconto/100
valor = mercadoria - des 
print(f'Desconto: {desconto:.2f}%')
print(f'Valor total: RS {valor:.2f}')