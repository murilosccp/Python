print("Todos os pares entre 1 e 50!")

'''for p in range(1, 51):
    par = p % 2
    if par == 0:
        print(p, end=' ')'''



for p in range(2, 51, 2):
        print(p, end=' ')    
#O professor mostrou a seguinte forma de fazer, que economiza processamento na CPU
#Basicamente ele começou direto no dois e foi pulando de 2 em 2 até o 50,
#Sem a necessidade de contar os ímpares.