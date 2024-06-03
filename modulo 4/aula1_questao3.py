n1=int(input("Valor de n1 é: "))
n2=int(input("Valor de n2 é: "))
n3=int(input("Valor de n3 é: "))

m=(n1+n2+n3)/3

if m<=60 and m>=40:
    print("Recuperação")
else:
    if m>=60:
        print("Aprovado")
    else:
        print("Reprovado")
print("Fim.")