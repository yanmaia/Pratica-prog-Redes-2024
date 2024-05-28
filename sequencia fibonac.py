#Faça um programa que exiba a Sequência de Fibonacci,O programa deverá solicitar um número que será a quantidadede elementos da Sequência de Fibonacci.

num= int(input('Informe a quantidade de elementos da sequencia fibonacci que deseja: '))
contador=1
n1=1
n2=1
while num >= contador:
    if contador <=2:
        print('1')
        contador+=1
    else:
        soma= n1 + n2
        n2 = n1
        n1= soma
        contador+=1
        print(soma)        
    
