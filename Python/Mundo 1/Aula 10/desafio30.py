print('!? PAR OU ÍMPAR ?!')
num = int(input('Digite um número para ver '))
ioup = num % 2

if ioup > 0:
    print("""
O número {} é ímpar!
    """.format(num))
else:
    print("""
O número {} é par!  
    """.format(num))

# Desafio concluido e logica certa HAHA
# só que ao ines de > o prof usou == mas no fim deu o msm