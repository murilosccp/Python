from datetime import date
print("MIRIM OU MASTER?")

ano = int(input("Digite seu ano de nascimento: "))

idade = date.today().year - ano

if idade <= 9:
    print("""O atleta tem {} anos 
Classificação: nadador MIRIM!""".format(idade))
elif idade < 15 and idade >= 10:
    print("""O atleta tem {} anos
Classificação: nadador INFANTIL!""".format(idade))
elif idade < 20 and idade >= 15:
    print("""O atleta tem {} anos
Classificação: nadador JÚNIOR!""".format(idade))
elif idade < 26 and idade >= 20:
    print("""O atleta tem {} anos
Classificação: nadador SÊNIOR!""".format(idade))
elif idade >= 26:
    print("""O atleta tem {} anos
Classificação: nadador MASTER!""".format(idade))