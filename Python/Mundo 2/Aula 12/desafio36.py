print('EMPRÉSTIMO!!!')
home = float(input('Digite o valor da casa que deseja comprar: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite em quantos anos você pagará: '))

naoExe = sal * 0.3

prestacao = (home / anos) / 12

cores = {
    'negado' : '\033[1;31m',
    'liberado' : '\033[1;32m',
    'limpa': '\033[m'
}

if prestacao > naoExe:
    print("""{}    !!! VALOR NEGADO !!!
Sinto muito mas o valor da prestação excede 30% do seu salário.
A prestação seria de {:.2f}
A operação não poderá ser concluida.{}
          """.format(cores['negado'], prestacao, cores['limpa']))
elif prestacao < naoExe:
    print("""{}    !!! VALOR LIBERADO !!!
Esse será o valor das suas prestações mensais: R${:.2f}
          {}""".format(cores['liberado'], prestacao, cores['limpa']))