a = int(input("Primeiro número:"))
b = int(input("Segundo número:"))
c = int(input("Terceiro número:"))

if a >= b and a >= c:
    maior = a

elif b >= a and b >= c:
    maior = b

else:
    maior = c

print ("Maior número:" , maior)