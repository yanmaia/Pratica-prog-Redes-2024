num=int(input("Informe um valor inteiro para transformarmos em binario."))
bin=[ ]
while num>0:
    resto=  num%2
    bin+=[resto]
    num//=2
print( "o numero binario e:",bin[::-1])