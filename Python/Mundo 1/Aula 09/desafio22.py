nome = str(input("Digite o seu nome completo paizão:  ")).strip()
nomeA = nome.upper()
nomea = nome.lower()
numSem = len(nome) - nome.count(' ')
firstName = nome.find(' ')
print("""
Esse é seu nome em CAPSLOCK: '{}'

Aqui ele em letras minusculas: '{}'

Essa é a quantidade de letras(sem espaço): {}

E aqui quantas letras tem o primeiro nome: {} 
""".format(nomeA, nomea, numSem, firstName))