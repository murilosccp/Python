import random 
print('!ESSE ALGORITMO APONTA QUEM É CORNO!')
n1 = str(input('Bobão 1: '))
n2 = str(input('Bobão 2: '))
n3 = str(input('Bobão 3: '))
n4 = str(input('Bobão 4: '))

lista = [n1, n2, n3, n4]

nome = random.choice(lista)
print('O Corno é {}'.format(nome))


#Console.WriteLine($"kjdfgkdfj {num}"+ kdj);
