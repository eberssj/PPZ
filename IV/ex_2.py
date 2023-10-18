import random

numeros = random.sample(range(100), 20)

pares = []
impares = []

for x in numeros:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print ("Todos os números: ", numeros)
print ("Números pares: ", pares)
print ("Númeris impares: ", impares)
