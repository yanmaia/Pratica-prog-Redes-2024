#Fazer um programa que solicite um número e calcule o seu fatorial

num= int(input('Digite o numero para fatoriar '))
soma=1
contador=1
if  num < 0:
    print('Informe um numero Natural para fatoriar:')
    quit()
else: 
    for num in range (1,num+1):
        soma =  soma* contador
        contador += 1    
print(soma)
