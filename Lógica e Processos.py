

numero_0_0=int(input("digite o primeiro valor de 1/9:"))
numero_0_1=int(input("digite o segundo valor de 2/9:"))
numero_0_2=int(input("digite o terceiro valor de 3/9:"))
numero_1_0=int(input("digite o quarto valor de 4/9:"))
numero_1_1=int(input("digite o quinto valor de 5/9:"))
numero_1_2=int(input("digite o sexto valor de 6/9:"))
numero_2_0=int(input("digite o sétimo valor de 7/9:"))
numero_2_1=int(input("digite o oitavo valor de 8/9:"))
numero_2_2=int(input("digite o nono valor de 9/9:"))

matriz_usuario=[[numero_0_0,numero_0_1,numero_0_2],
        [numero_1_0,numero_1_1,numero_1_2],
        [numero_2_0,numero_2_1,numero_2_2]]

for i in range(0,len(matriz_usuario)):
    print (matriz_usuario[i])

numero_pares=0
for i in range(0,3):#dentro da lista
    for j in range(0,3):#dentro de colunas
        matriz_usuario[i][j]
        if matriz_usuario[i][j]%2==0:
            numero_pares=numero_pares+matriz_usuario[i][j]
    else:
        print("Número ímpar")
    print("Esse é o resultado da soma dos números pares: ", (numero_pares))

soma_valores=(matriz_usuario[2][0]+matriz_usuario[2][1]+matriz_usuario[2][2])
print("a soma dos valores da terceira coluna é igual a: ",(soma_valores))

maior_valor=max(matriz_usuario[1])
print("o maior valor da segunda linha é:", (maior_valor))