from random import randint
from time import sleep
print('{:^40}'.format("""PEDRA, PAPEL e TESOURA"""))

jog = int(input("""Faça sua escolha:!
        [0] PEDRA 
        [1] PAPEL       
        [2] TESOURA
Qual é a sua jogada? """))

lis = ('Pedra', 'Papel', 'Tesoura')
num = randint(0, 2)

if jog not in (0, 1, 2):
    print("""MEU MANO EM CRISTO ENFIA ESSE {} NA SUA BUNDA!
    """.format(jog))
else:
        
   print('JO')
   sleep(0.8)
   print('KEN')
   sleep(0.8)
   print('PO!!!')
   sleep(0.4)

   print("""
Jogador Jogou: {}
E o Computador Jogou: {}""".format(lis[jog], lis[num]))

   if jog == num:
        print("""
HOUVE EMPATE HAHAHA""")
                
   elif (jog - num) % 3 == 1:
        print("""
VITÓRIA DO JOGADOR HAHA""")   

   else:
       print("""
COMPUTADOR GANHOU PAIZÃO HAHA""")