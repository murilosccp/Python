from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
sen = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print('O valor de seno é {:.4f}\nde cosseno é {:.4f}\ne da tangente desse ângulo é de {:.4f}'.format(sen, coss, tang))


# Minha maneira estava correta, porém faltava converter os valores de sin, cos e tan
# para radianos usando a função "radians". Um ponto inteiressante, não sabia disso. 