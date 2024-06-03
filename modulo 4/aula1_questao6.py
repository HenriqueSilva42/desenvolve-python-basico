
n=int(input("Quantos experimentos foram feitos?: "))
cont=0
qnt=0
c=0
r=0
s=0 

while n > cont:
    qnt,tipo = input('Digite a quantidade de animais e o tipo coelho(C),rato(R) ou sapo(S)?: ').split(" ")
    qnt=int(qnt)
    cont =cont+1
    if tipo=="C":
        c=c+qnt
    elif tipo=="R":
        r=r+qnt
    elif tipo=="S":
        s=s+qnt
    else:
        print("Tipo inválido, tente novamente!")
        cont=cont-1

print("Total: %i cobais: "% (s+r+c))
print("Total de coelhos: %i  "% c)
print("Total de ratos: %i  "% r)
print("Total de sapos: %i  "% s)
print("Percentual de coelhos: %2.2f%%"% (100*c/(s+r+c)))
print("Percentual de ratos: %2.2f%%"% (100*r/(s+r+c)))
print("Percentual de sapor: %2.2f%%"% (100*s/(s+r+c)))
        
