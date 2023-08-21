print("!!! MAIOR E MENOR !!!")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("""
O PRIMEIRO valor {} é o maior que o segundo valor {}!""".format(num1, num2))
elif num2 > num1:
    print("""
O SEGUNDO valor {} é o maior que o primeiro valor {}!""".format(num2, num1))
elif num1 == num2:
    print("""
 Os valores {} e {} são iguais :)""".format(num1, num2))
