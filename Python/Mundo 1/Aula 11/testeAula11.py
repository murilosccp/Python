# td código de cor no python começa com o \033 dentro do "" e no final da frase pra cor ficar só nas palavras.
# onde dentro do [ vão ficar: style; text; back e o 'm' no fim. 
# As especificações de style do texto são:
# 0 = none, 1 = bold, 4 = underline e 7 para negativo que deixa a letra preta.
# Depois do style, temos o text que muda a cor do texto sendo eles:
# 30 = white, 31 = red, 32 = green, 33 = yellow, 34 = blue, 35 = purple, 36 = cyan e 37 = gray.
# Para outras cores é necessario uma biblioteca.
# e em Back = background temos 8 planos de fundo sendo eles: 
# 40 = white, 41 = red, 42 = green, 43 = yellow, 44 = blue, 45 = purple, 46 = cyan e 47 = gray.
# \033[m = ele retorna á configuração do terminal.
# pesquisar a função colorize no python


#print("\033[7;30;40mOlá mundo!\033[m")

#a = 4
#b = 5
#print("Os valores são \033[31;43m{}\033[m e \033[33;41m{}\033[m".format(a, b))

#nome = 'Murilo Lindo'
#print("Prazer em te conhecer, {}{}{}!!!".format('\033[4;33;40m', nome, '\033[m')) # É possivel colocar cor somente da na variavel de manteira mais fácil.


cores = {
    'limpa': '\033[m',
    'azul' : '\033[34m',
    'amarelo' : '\033[1;33m',
    'corinthians' : '\033[7;30m'
}
nome = ('Murilo Lindo')
print("Prazer em te conhecer, {}{}{}!!!".format(cores['amarelo'], nome, cores['limpa']))
# Maneira mais organizada de coloca cor no código.