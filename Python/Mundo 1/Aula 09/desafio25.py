nome = str(input("Digita teu nome e vamo vê se tem Silva: ")).strip()
min = nome.capitalize()
veriName = 'silva' in min

print(""" 
seu nome tem 'Silva' = {}
""".format(veriName))