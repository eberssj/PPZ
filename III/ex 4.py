n = int(input('Diite o numero: '))
a, b = 1, 1
k = 1
while k <= n - 2:
    a, b = b, a + b
    k = k + 1

print(b)
