print("VIRA UM TRIÂNGULO?")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a < b + c and b < a + c and c < a + b:
    print("""
Estes números podem formar um triângulo! :)    
    """)
else: 
    print("""
Estes número não podem formar um triângulo :(
    """)

