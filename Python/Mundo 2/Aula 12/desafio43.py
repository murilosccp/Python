print("CALCULADORA DE IMC!")
peso = float(input("Digite o seu peso em KG: "))
alt = float(input("Digite a sua altura em M: "))

imc = peso / (alt ** 2)

print("o IMC dessa pessoa é de {:.1f}".format(imc))

if imc < 18.5:
    print("Cuidado você está abaixo do peso normal!")
elif imc < 24.9 and imc >= 18.5:
    print("Meus parabéns você está no peso normal!")
elif imc < 29.9 and imc >= 25:
    print("Cuidado vc está com excesso de peso!")
elif imc < 34.9 and imc >= 30:
    print("CUIDADO VC ESTÁ COM OBESIDADE CLASSE I")
elif imc < 39.9 and imc >= 35:
    print("CUIDADO VC ESTÁ COM OBESIDADE CLASSE II")
elif imc >= 40:
    print("CUIDADO VC ESTÁ COM OBESIDADE CLASSE III")