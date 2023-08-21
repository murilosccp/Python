sal = float(input("Digite seu salario e veja quanto de aumento terá: "))

rea = (sal / 100) * 10
reaa = (sal / 100) * 15
sal1 = rea + sal
sal2 = reaa + sal

if sal > 1250:
    print("""
Seu novo salario será de: {} R$
Um aumento de: {:.2f} R$ 10%
    """.format(sal1, rea))
else:
    print("""
Seu novo salario será de: {} R$
Um aumento de: {:.2f} R$ 15% 
    """.format(sal2, rea))