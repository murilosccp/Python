frase = 'murilo bobo'
separado = frase.replace (" ", "")
print(frase.upper(), frase.lower(), len(separado))
#print("""Aqui ele pegou e separou as palavras em listas então chamai a lista 0 e pedi que me 
#mostrasse o caracter 4 dela que no caso é o 'L' FAZ O L! """)

#print("""Aqui eu digito um exemplo de pra que serve as 3 aspas juntas, basicamente elas servem
#para não precisarmos criar um trilhão de 'print's' para cada linha do código, algo bem legal e
#simples que ajuda muito com certeza!""")

# !26/06/23 AULA!
# frase [9] esse tipo de fatiamento pega somente um caracter dentro da String que está alocada na memória.
# frase [3:10] esse tipo de fatiamento pega do 3 até o 10 mas o caracter 10 ele exclui e não conta.
# frase [3:11] ele só pega até aonde existe se colocar um valor um valor maior do que existe ele ajusta automaticamente.
# frase[3:10:2] nesse tipo ela vai do 3 até o 10 pulando de duas em duas casas.
# frase[:3] aqui ele começa do 0 e vai até o 3, não incluindo o valor de 3.
# frase[::3] aqui vai pulando de 3 em 3 até o final
# frase [3:] ele vai do 3 até o fim.
# frase [3::3] começa no 3 e vai pulando de 3 em 3 casas até o final.
# len(frase) a função (len)ght calcula e diz o tamanho da variavel em caracteres. (fora isso consigo utilizar a função de ver o tamanho e fatiar ao mesmo tempo).
# frase.count('o') nesse caso essa função contaria quantas vezes aparece a letra "o" na string.
# frase.count('o', 0, 8) aqui ele conta do 0 até o fim da string quantos "o" temos nesse espaço selecionado.
# frase.find('ilo') ele mostra em que momento começa o "ilo", que no caso começa no microespaço 3. 
# frase.find('Android') se colocar uma string que não existe ele retorna o valor -1.
# 'murilo' in frase o operador "in" verifica se existe ou não a string digitada.
# frase.replace ('murilo', 'Android') aqui ele subistitue a string por outra. (Não de forma permante).
# frase = frase.replace ('murilo', 'Android') aqui ele muda e salva as alterações.
# frase.upper() aqui ele vai transformar os caracteres em MAIUSCULO, oq é maisculo fica e oq não é vira.
# frase.lower() aqui ele vai transformar os caracteres em minusculo, oq é minusculo fica e oq não é vira.
# frase.capitalize() só o primeiro caracter das strings ficam em Maiusculo.
# frase.title() ele transforma os caracteres que começam as palavras em Maiusculo.
# frase.strip() ele remove os espaços inuteis das strings, transformando os espaços em nada e contando do 0 a partir da primeira letra.
# frase.rstrip() aqui ele remove os espaços do lado R ou seja somente na direita.
# frase.lstrip() aqui ele remove os espaços do lado L ou seja somente na esquerda.
# frase.split() estudar melhor essa função, ela pega e divide a striing aonde tem um espaço, gerando uma lista para cada palavra.
# '-'.join(frase) ele junta todos os elementos da frase e junta os espaçando pelo "-".
