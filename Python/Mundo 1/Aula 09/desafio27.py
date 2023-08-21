nome = str(input("Digite seu nome: ")).strip().capitalize()
name = nome.split()


name1 = name[0]
name2 = name[-1].capitalize()



print(""" 
Aqui está o seu primeiro nome: '{}'
E aqui o ultimo nome: '{}' 
""".format(name1, name2))