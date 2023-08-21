import random
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
nome = random.choice(lista)
print('O aluno escolhido foi {}'.format(nome))

# Pelo que entendi estava fazendo errado pois o modulo "random" tem uma 
# função chamada "choice" a qual não estava utilizando e por isso o erro
# aparecia, além de que eu tbm não tinha feito essa lista, será que ela 
# transforma as Strings em valor numérico? Não sei kkkkkkkk