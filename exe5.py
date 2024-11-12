#Faça um programa que peça dois números, base e expoente, calcule e
# mostre o primeiro número elevado ao segundo número


n=int(input("Digite um valor: "))
m=int(input("Digite outro valor: "))

h=n
rs=0
for i in range(0,m-1):
    h=h*n

    print("O resultado da exponenciação é: "+str(h))