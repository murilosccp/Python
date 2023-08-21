print("VAMO VER SE PASSOU")

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

cores = {
    'reprovado' : '\033[1;31m',
    'aprovado' : '\033[1;32m',
    'limpa': '\033[m'
}

if media < 5:
    print("{}Sua média é de {:.1f} insuficiente REPROVADO!{}".format(cores['reprovado'], media, cores['limpa']))
elif media < 7 and media >= 5:
    print("Sua média de {:.1f} está abaixo, você vai pra RECUPEAÇÃO!".format(media))
elif media >= 7:
    print("{}Com sua média de {:.1f} você foi APROVADO parabéns!{}".format(cores['aprovado'], media, cores['limpa']))