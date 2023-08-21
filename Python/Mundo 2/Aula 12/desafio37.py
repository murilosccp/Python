print("CONVERSÃO HAHA")

num = int(input("Digite um númeiro inteiro: "))
choice = int(input("""
Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """))

bina = bin(num)[2:]
oc = oct(num)[2:]
hexa = hex(num)[2:]

if choice == 1:
    print("{} convertido para BINÁRIO é: {}".format(num, bina))
elif choice == 2:
    print("{} convertido para OCTAL é: {}".format(num, oc))
elif choice == 3:
    print("{} convertdo para HEXADECIMAL é: {}".format(num, hexa))
else:
    print("MEU MANO EM CRISTO ENFIA ESSE {} NA SUA BUNDA!".format(choice))
    

