from datetime import date
print("CALCULO DE ANO BISSEXTO")
ano = int(input("Insira o ano ou digite 0 para selecionar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print("""
O ano de {} não é um ano bissexto :(  
    """.format(ano))
else:
    print("""
O ano de {} é um ano bissexto!! :)  
    """.format(ano))

# Acertei mas me perdi em outros comandos que ele passou haha, mas deu certo
# e ainda por cima aprendi and e or.