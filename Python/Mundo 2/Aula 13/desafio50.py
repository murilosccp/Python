print("SOMA de PARES")
s = 0
con = 0
for p in range(1, 7):
    n = int(input("Digite o {}º valor para a soma: ".format(p)))
    par = n % 2
    if par == 0:
        s += n
        con += 1
print("""A soma dos {} números PARES é de: {}!!
""".format(con, s))