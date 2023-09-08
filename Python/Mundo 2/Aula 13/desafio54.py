from datetime import datetime
print("GRUPO DA MAIORIDADE")
adultos = 0
menores = 0
for p in range(1, 8):
    ano = int(input("Digite o ano em que a {}ª pessoa nasceu? ".format(p)))
    idade = datetime.now().year - ano
    if idade >= 18:
        adultos += 1
    else:
        menores += 1
if menores == 0:
    print("""
Ao todo tivermos {} adultos
E NENHUM menor, só véio KKKKKKKK""".format(adultos))
elif adultos == 0:
    print("""
Não tivemos NENHUM adulto, mas tivemos {} menores!
A criançada reina! KKKKKKKKK""".format(menores))
elif adultos and menores >= 1:    
    print("""
Ao todo tivermos {} adultos
E {} menores!""".format(adultos, menores))