import random
from time import sleep 
print("""
Vou pensar em um número entre 0 e 5, tente advinhar!
""")
adv = int(input('Digite um número e veja se acertou! '))
lista = [0, 1, 2, 3, 4, 5]
num = random.choice(lista)

print('PROCESSANDO...')
sleep(3)
if adv == num:
    print("""
Meus parabéns vc é um verdadeiro advinha HAHA!   
    """)
else:
    print("""
Poxa não foi dessa vez, eu pensei no número {} e não no {}!  
    """.format(num, adv))    

print('FIM DE JOGO!')

# o professor usou assim: from random import randint
# num = randint(0, 5)
# basicamente ele só puxou uma funçao do modulo random eu puxei td acho que é mais fácil mas manterei minha forma.
# Desafio concluido e certo HAHA!
#