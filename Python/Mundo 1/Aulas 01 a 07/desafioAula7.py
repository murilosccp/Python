n1 = int(input('Digite um valor: '))
n2 = int(input('Agora outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
re = n1 % n2
me = n1 - n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {}'.format(s, m, d, di), end=' ')
print('A potência é {}, o resto da divisão é {}, e a subtração é {}'.format(e, re, me))







## Cada operador abaixo precisa de dois operandos
## para funcionar corretamente, com 2+5.
## == para receber o valor da conta.

## + = adição, - = menos, * = multiplicação
## / = divisão, ** = potência, // = divisão inteira
## % = resto da divisão

## Ordem de Precedência:
## 1º () resolver os parenteses
## 2º **  logo depois as potência
## 3º *, /, //, % seguir nessa exata ordem
## 4º +, - mais e menos sempre por ultimo.

