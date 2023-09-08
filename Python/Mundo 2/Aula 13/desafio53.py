print("?PALÍNDROMO OU NÃO?")
frase = str(input("Digite uma frase: ")).strip().lower()
palavras = frase.split()
união = ''.join(palavras)
inv = ''
for caracter in range(len(união) -1, -1, -1):
    inv += união[caracter]
print('''O inverso de {} é {}'''.format(união, inv))
if inv == união:
    print("""A frase é um Palíndromo HAHA""")
else:
    print("""A frase NÃO é um Palíndromo :(""")