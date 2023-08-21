print('{:=^40}'.format(" LOJA WOLFGAME "))

preco = int(input("Valor das compras: R$"))
while True:
    
    opc = int(input("""FORMAS DE PAGAMENTO
    [1] à vista dinheiro/pix
    [2] à vista cartão
    [3] 2x no cartão SEM JUROS
    [4] 3x ou mais no cartão COM JUROS de 20%
Sua Escolha: """))

    if opc == 1:
        desc = (preco / 100) * 10 
        newpri = preco - desc
        print("""
Com a opção de pagar com dinheiro/PIX você ganhou um desconto de 10%!!
Agora o valor da sua compra passa de R${:.2f} e vai para R${:.2f}
    """.format(preco, newpri))
        break

    elif opc == 2:
        desc2 = (preco / 100) * 5
        newpri2 = preco - desc2
        print("""
Com a opção de pagar à Vista na Cartão você ganhou um desconto de 10%!!
Agora o valor da sua compra passa de R${:.2f} e vai para R${:.2f}
    """.format(preco, newpri2))
        break

    elif opc == 3:
        parcel = preco / 2
        print("""
Você selecionou a opção de pagar parcelado em 2x no cartão
Você deve pagar duas parcelas de R${:.2f}
    """.format(parcel))
        break

    elif opc == 4:
        print("Você selecionou a opção de pagar em 3x ou mais no cartão.")
        while True:
            parce = int(input("""
Em quantas parcelas deseja pagar? """))
            if parce < 3:
                print("""IRMÃO EM CRISTO SÓ PODE PAGAR EM 3X OU MAIS!""")
            else:
                juros = (preco / 100) * 20
                newpri3 = preco + juros
                parcel = newpri3 / parce
                print("""
Sua compra foi parcelada em R${}x de R${:.2f} COM JUROS!
A sua compra no valor de R${:.2f}, agora será de R${:.2f} com os juros.
    """.format(parce, parcel, preco, newpri3))
                break
        break
            
    else:
        print("""MEU MANO EM CRISTO ENFIA ESSE {} NA SUA BUNDA!
    """.format(opc))