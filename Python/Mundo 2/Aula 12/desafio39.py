from datetime import date
print("ALISTAMENTO")
choice = int(input("""
Primeiro informe seu SEXO:
[ 1 ] Se você for homem
[ 2 ] Se você for mulher
Sua opção: """))

if choice == 1:
    print("----------- :( HOMEM ): -----------")
    ano = int(input("Digite o ano do em que nasceu: "))

    idade = date.today().year - ano
    cal = idade - 18
    cal2 = 18 - idade
    dev = ano + 18

#posso colocar as variaveis acima dentro para deixar melhor a compreensão 

    if cal > 0:
        print("""
Quem nasceu em {} tem {} anos em {}
Você deveria ter se alistado a {} anos amigão BORA!
Seu alistamento foi em {}
    """.format(ano, idade, date.today().year, cal, dev))
    elif cal < 0:
        print("""
Quem nasceu em {} tem {} anos em {}          
Ainda faltam {} anos para o seu alistamento!
O ano do seu alistamento vai ser em {}
    """.format(ano, idade, date.today().year, cal2, dev))
    elif cal == 0:
        print("""
Quem nasceu em {} tem {} anos em {}
Esse é o seu ano de alistamento VÁ AGORA!
    """.format(ano, idade, date.today().year, cal))

elif choice == 2:
    print("----------- (: MULHER :) -----------")
    print("""
Você é uma linda mulher e não é obrigatorio se alistar.
Tenha um bom dia!!
""")