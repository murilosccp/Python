frase = str(input("Digite uma frase: ")).strip().lower()
word = frase.split()
juntar = ''.join(word)
inv = juntar[::-1]
print('''O inverso de {} é {}'''.format(juntar, inv))
if inv == juntar:
    print("""A frase é um Palíndromo HAHA""")
else:
    print("""A frase NÃO é um Palíndromo :(""")