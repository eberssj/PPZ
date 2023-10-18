a = int(input('valor de a: '))
b = int(input('valor de b: '))
while a % b != 0:
    a, b = b, a % b
print(f'valor do mdc: {b}')
