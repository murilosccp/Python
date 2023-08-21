print("QUAL O MAIOR E O MENOR")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print("""
O menor número é o {}
""".format(menor))

print("""E o maior número é o {}""".format(maior))