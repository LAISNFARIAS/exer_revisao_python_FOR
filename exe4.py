numeros=[]
for a in range (0,5):
 soma =int(input("Informe um valor: "))
numeros.append(soma)
m=numeros[0]
for a in numeros:
    if a > m:
        m=a

    print("O maior valor é ", m) 