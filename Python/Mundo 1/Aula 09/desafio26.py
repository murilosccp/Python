frase = str(input("Digite uma frase qualquer: ")).strip()
frasemin = frase.lower()
cont = frasemin.count('a', 0)
achou = frasemin.find('a')+ 1
achei = frasemin.rfind('a')+ 1

print(""" 
Na sua frase os A's aparecem {} vezes
Sendo o primeiro deles na posição: {}
E o ultimo na posição: {}.
""".format(cont, achou, achei))
