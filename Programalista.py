num=int(input('informe um numero Para adicionarmos na lista'))
lista=[num]
while num != 0 :  
    num=int(input('informe um numero Para adicionarmos na lista'))
    lista.append(num)
lista.sort()
soma=sum(lista)
print(f'Foi digitado {len(lista)} numeros\nO valor da soma e {soma}\nA media e {(sum(lista)/len(lista))}\nEssa lista esta na ordem {lista}')
