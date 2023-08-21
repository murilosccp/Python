print("Soma de TODOS os ÍMPARES!")
con = 0
soma = 0
for i in range(1, 501, 2): 
    if i % 3 == 0:
        con += 1
        soma += i
print("A soma dos {} valores, deu um total {}".format(con, soma))