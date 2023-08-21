nome = str(input("Digite seu nome: ")).strip().capitalize()

if nome == 'Murilo':
    print("Que nome lindo e maravilhoso!")
elif nome == 'Pedro' or nome == 'Maria':
    print ("Nome popular em slc kkkkkkk")
elif nome == 'Betina':
    print("Nossa vc tem o nome da Garota mais linda do mundo!!")
else:
    print("Nome normal em :/")
print("Tenha um bom dia {}!".format(nome))