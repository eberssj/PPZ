cont = 0

for numero in range (1067, 3627):
    if numero % 2 == 0 and numero % 7 == 0:
        cont += 1

print (cont)