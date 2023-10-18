import random

numeros = random.sample (range(100), 10)
maior = 0 
menor = 100

for item in numeros:
    if item > maior:
        maior = item 
    if item < menor:
        menor = item
    
print(numeros)
print(maior)
print(menor)

