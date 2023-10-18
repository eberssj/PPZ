import math

metrosporlitro = 3 
litrosporlata = 18  

metrospintados = float(input("Metros a serem pintados: "))
totaldelitros = metrospintados / metrosporlitro
numerodelatas = math.ceil(totaldelitros / litrosporlata)
precototal = numerodelatas * 80

print(f"Quantidade de latas necessárias: {numerodelatas}")
print(f"Preço total: R$ {precototal:.2f}")
