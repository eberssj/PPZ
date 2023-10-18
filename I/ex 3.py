dias = int(input("Numero de dias:"))
horas = int(input("Numero de horas:"))
minutos = int(input("Numero de minutos:"))
segundos = int(input("Numero de minutos:"))

resultadodias = dias * 86400
resultadohoras = horas * 3600
resultadominutos = minutos * 60

print("Resultado final:" , (resultadodias + resultadohoras + resultadominutos + segundos))
