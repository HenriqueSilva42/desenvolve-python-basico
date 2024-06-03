n=int(input("Valor de N é: "))
maior=0
while n>0:
        x=int(input("Valor de x é: "))
        if x>maior:
            maior=x
            n -= 1
        else:
            n -= 1
else:
    print(maior)