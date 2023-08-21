print('!ATENÇÃO O VALOR DA MULTA É DE 7 REAIS POR CADA KM ACIMA DO LIMITE!')
vel = float(input('Digite a velocidade que você estava '))

multa = (vel - 80) * 7

if vel < 80.0:
    print("""
Você está dentro do limite de 80km/h! 
Sem multas.   
    """)
    
else:
    print("""
PI PI PI TÁ MULTADO FAAAZ O L KKKKKKKKKKKK
OLHA A MULTA DE R${:.2f} 
    """.format(multa))


# Desafio concluido e lógica certa HAHA
# refinamento sucessivo 