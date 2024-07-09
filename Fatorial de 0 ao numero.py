num= int(input('Digite o numero para fatoriar '))           #Fazer um programa que solicite um número calcule o fatorial de cada numero entre  0 e  o numero informado
if  num < 0:
    print('Informe um numero Natural para fatoriar:')
    quit()
else: 
    for i  in range (num+1):
        soma=1
        contador=1
        for l in range (1,i+1):
            soma =  soma* contador
            contador += 1    
        print(f" a fatoração do numero {i} e: ",soma)
