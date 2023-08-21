print("VIRA UM TRIÂNGULO?")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a < b + c and b < a + c and c < a + b:
        print("""
Estes números podem formar um triângulo! """)
        if a == b == c:
                print("""
E por serem iguais podem formar um Triângulo Equilátero! :)    
    """)
        elif a == b or b == c or c == a:
               print("""
Mas como somente dois lados são iguais será um Triângulo Isósceles! :)
""")
        elif a != b and b != c and c != a:
               print("""
Mas como são diferentes será um Triângulo Escaleno! :)
""")
else: 
    print("""
Estes número não podem formar um triângulo :(
    """)

# a != b != c != a deixa mais simples a resolução.
#
#