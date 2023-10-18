cigs = float(input("Quantidade de cigarros por dia:"))
anos = float(input("Quantidades de anos fumados:"))
totalcigs = cigs * anos * 365
totaldiasperd = totalcigs/144
print(f'Dias perdidos: {totaldiasperd:.2f}')