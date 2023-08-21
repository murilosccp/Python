print("VIAGENS ACIMA DE 200 KM DE DISTÂNCIA TEM DESCONTO DE 5 CENTS")
dis = int(input("Qual a distãncia da sua viagem? Em Km's: "))

v1 = dis * 0.5
v2 = dis * 0.45

if dis <= 200:
    print("""
Esse é o preço da sua viagem: R${:.2f}    
    """.format(v1))
else:
    print("""
Esse é o preço da sua viagem com desconto: R${:.2f}
    """.format(v2))

# Acertei