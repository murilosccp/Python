"""for c in range(6, 0, -1):
    print('VAI SE FUDER ROGER GUEDES CALVO FDP')
print("CABO")"""

# No final ali onde está o -1 é onde ocorre a interação do que queremos
# pode ser ele tirando um numero para contar do maior para o menor ouu
# falando pra ele contar de um número pra outro pulando duas casas.


"""i = int(input("inicio: "))
f = int(input("Fim: "))
p = int(input("Passos: "))

for c in range(i, f+1, p):
    print(c)
print("FIM")"""

#acima o programa conta o número inicial, o número final e em quantos passos ele vai fazer
#seja de 1 em 1 de 2 em 2 e assim por diante

s = 0
for c in range(0, 6):
    n = int(input("Digite os números para a soma: "))
    s += n
print("A soma dos Seis números é de: {}".format(s))