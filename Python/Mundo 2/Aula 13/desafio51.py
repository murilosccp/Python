print("""PROGRESSÃO ARITMÉTICA!!!""")
termo = int(input("Digite o 1º Termo: "))
razão = int(input("Digite a Razão: "))
decimo = termo + (10 - 1) * razão
for pa in range(termo, decimo + razão, razão):
    if pa != decimo:
        print(pa, ' → ', end='')
    else:
        print(pa)




'''primeiro = int(input("Digite o 1º Termo: "))
razão = int(input("Digite a Razão: "))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print("{} ".format(c), end=' → ')'''