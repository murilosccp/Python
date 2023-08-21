#nome = str(input('Qual o seu nome? ')).strip().capitalize()
#if nome == "Murilo":
#    print('Que nome lindo mano, é isso somos irmãos de nome!')
#else:
#    print('Bah acontece {}, na proxima tu vem como um Murilo!'.format(nome))

#print('''
#Aqui {} é o print que sempre vai mostrar independente da condição do IF!
#'''.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/ 2

if m >= 6:
    print("""
Parabéns vc teve uma média satisfatória!! """)
else: 
    print("""
Lamentamos sua média foi insatisfatória :( """)

print('Continue se esforçando independentemente de qualquer coisa!')    