print("É Primo ou Não?")
num = int(input("Digite um número: "))

if num <= 1:
        print("Você digitou o núemro {}, e ele NÃO é um número primo.".format(num))
else:
    divi = 0
    primo = True
    for p in range(1, num + 1):
        if num % p == 0:   
            primo = False
            divi += 1
            print("\033[32m{}\033[0m".format(p), end=' ')
        else:
            print("\033[31m{}\033[0m".format(p), end=' ')
    if divi <= 2:
         print("""
O Número {} é PRIMO!!
Ele foi divisível {} vezes.""".format(num, divi))
    else:
         print("""
O Número {} NÃO é PRIMO!
Ele foi divisível {} vezes.""".format(num, divi))
         

#Código do professor:

"""print("É Primo ou Não?")
num = int(input("Digite um número: "))

if num <= 1:
        print("Você digitou o núemro {}, e ele não é um número primo.".format(num))
else:
    div = 0
    for p in range(1, num + 1):
        if num % p == 0:
            print('\033[33m]', end='')
            div += 1
        else:
            print('\033[31m]', end='')
        print('{} '.format(p), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, div))
if div == 2:
    print('Por isso ele é PRIMO!!')
else:
    print('Por isso ele NÃO é PRIMO!!')"""
         
