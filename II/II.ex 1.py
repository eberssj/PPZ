a = int(input("Valor um:"))
b = int(input("Valor dois:"))
c = int(input("Valor tres:"))

if a > b + c or b > a + c or c > a + b:
    print("Não é um triangulo!")

elif a == b == c:
    print("É um equilátero!")

elif a == b != c or b == c != a or c == a != b:
    print("É um isosceles!")

else:
    print("É um escaleno!")