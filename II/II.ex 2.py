from calendar import isleap
ano = int(input("Ano:"))

if isleap(ano):
    print("É bissexto!")

else:
    print("Não é bissexto!")