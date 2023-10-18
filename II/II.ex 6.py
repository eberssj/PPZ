hora = float(input("Salário por hora:"))
mes = float(input("Horas trabalhadas no mês:"))
salariobruto = hora * mes
impostoderenda = salariobruto * 11/100
inss = salariobruto * 8/100
sindicato = salariobruto * 5/100

salarioliquido = salariobruto - impostoderenda - inss - sindicato

print (f'Salário bruto: R$ {salariobruto:.2f}')
print (f'Imposto de renda: R$ {impostoderenda:.2f}')
print (f'INSS: R$ {inss:.2f}')
print (f'Sindicato: R$ {sindicato:.2f}')
print (f'Salário líquido: R$ {salarioliquido:.2f}')
