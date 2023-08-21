n = int(input("Digite o número que deseja multiplicar: "))
print("""Tabuada do {}!!""".format(n))    
for t in range(1, 11):
   tab = n * t
   print("""{} X {} = {}""".format(n, t, tab))