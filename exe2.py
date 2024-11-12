# Faça um programa que leia 5 números e informe a soma e a média dos números:

numeros=[]
for y in range (0,5):
    n= float(input("Digite um número: "))
    print(numeros)
    numeros.append(y) #append = adicioanar
    soma=0
    for i in numeros:
        soma+=i


print("A soma dos números é: "+str(soma))
print("A média dos números é: "+str(soma/len(numeros)))