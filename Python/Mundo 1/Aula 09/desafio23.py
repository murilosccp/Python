num = int(input("Digite um número de 0 a 9999 aí paizão: "))

numUni = num // 1 % 10
numDez = num // 10 % 10
numCen = num // 100 % 10
numMil = num // 1000 % 10

print("""
° Unidade: {}
° Dezena:  {}
° Centena: {}
° Milhar:  {}

O numero {} possui {} unidades, {} dezenas
{} centenas e {} milhares.""".format(numUni, numDez, numCen, numMil, num, numUni, numDez, numCen, numMil))