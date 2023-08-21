city = str(input("Digite o nome de uma cidade e direi se começa com 'Santo' ou não: ")).strip()
cap = city.capitalize()
verify = 'Santo' in cap

print("""
sua cidade é santa? = {}
""".format(verify))

#desafio correto mas esqueci o str e o strip