from time import sleep

choice = int(input("""Pronto pra contagem regressiva de 0 a 10?
SIM [1]
NÃO [2]
: """))

if choice == 1:
    sleep(0.9)
    print("ENTÃO VAMOS LÁ")
    sleep(0.9)
    print("PREPARAR")
    sleep(1)
    print("""APONTAR""")
    sleep(1)
    print("""JÁ!!!!""")
    sleep(0.5)
    for cr in range(10, -1, -1):
        print(cr)
        sleep(1)
    print("""🎆🎆🎆
CONTAGEM REGRESSIVA CONCLUÍDA!
🎇🎇🎇KABOOM!🎇🎇🎇 
🎆🎆🎆""")

elif choice == 2:
    print("""Você escolheu não iniciar a contagem. CANALHA!""")

else:
    print("Meu mano esse {} não pode, escolha entre 1 ou 2 ".format(choice))