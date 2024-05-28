num= int(input('Informe um numero inteiro: '))
for i in range (num + 1):      # mostra
    for j in range (i+1):
        print(j,end=' ')  # end= faz a junçao do print seguinte pelo espaço designado, enquanto j esta printando o valor de i e j
    print()


      