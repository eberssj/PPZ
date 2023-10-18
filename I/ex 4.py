salario = float(input("Salário:"))
porcentagem = float(input("Porcentagem de aumento:"))
aumento = salario/100 * porcentagem + salario
print(f'novo: RS {aumento:.2f}')