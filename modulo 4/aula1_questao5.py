"""
Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes.
Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente.
 Ao final, imprima a média das idades.
(idade1 + idade2 + idade3 + … + idade_n)/N
"""
n=int(input("Digite o número de pessoas entrevistadas?: "))
cont=0
soma=0
idade=0
while cont < n:
    idade=int(input("Idade: "))
    soma=soma+idade
    cont += 1
else:
    print("A média de todas as idades é:",soma/n)