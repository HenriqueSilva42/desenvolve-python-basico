#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e
#calcule a menor quantidade possível de notas necessárias para pagar aquele valor.
#As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 
#Entrada:
#576
#Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00


quantia=int(input("Digite um valor inteiro referente a uma quantia em reais"))

notas100= quantia //100 #divisão por inteiro de 100 os mesmo se repete pros outros valores
quantia= quantia % 100 #resto da divisão por 100 mesmo se repete pros outros valores

notas50= quantia //50 
quantia= quantia % 50

notas20= quantia //20 
quantia= quantia % 20

notas10= quantia //10
quantia= quantia % 10

notas5= quantia //5 
quantia= quantia % 5

notas2= quantia //2 
quantia= quantia % 2

notas1= quantia //1 
quantia= quantia % 1


print((f"{notas100} de R$100,00"))
print((f"{notas50} de R$50,00"))
print((f"{notas20} de R$20,00"))
print((f"{notas10} de R$10,00"))
print((f"{notas5} de R$5,00"))
print((f"{notas2} de R$2,00"))
print((f"{notas1} de R$1,00"))