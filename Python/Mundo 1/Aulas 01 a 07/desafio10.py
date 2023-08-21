money = int(input('Digite o valor para saber quantos dolares pode comprar!: '))
cambio = 5.24

dolar = money / cambio
print('Você possui {}, e você pode comprar até {:.2f} de dolares!'.format(money, dolar))
