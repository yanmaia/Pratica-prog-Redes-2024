n = int(input("Digite um valor inteiro e positivo para n: "))
if n <= 0:
    print("O valor de n deve ser positivo e diferente de zero.")
else:
    soma = 0
    termos = ""
    for i in range(1, n+1):
        termo = 1 / i
        soma += termo
        termos += f"1/{i}" if i == 1 else f" + 1/{i}"
        print(f"Termo {i}: 1/{i} = {termo}")
    print(f"A soma dos termos ({termos}) é igual a {soma}.")