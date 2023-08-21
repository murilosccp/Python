dias = float(input("Quantos dias alugou o carro? "))
km = float(input("Quantos Km rodou? "))
pdia = dias * 60
pkm =  km * 0.15
preco = pdia + pkm
print("o total a pagar é de R${}".format(preco))


# forma do professor: //preco = (dias * 60) + (km * 0.15)\\, mais facil e 
# que simplifica o código tenho que pensar mais assim.. o importante
# é que acertei.