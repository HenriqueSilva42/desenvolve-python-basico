"""
Escreva um programa em Python que utiliza a biblioteca random para gerar
 um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número.
Forneça feedback se o palpite é muito alto, muito baixo ou correto. 
Interrompa a execução somente quando o usuário acertar o palpite.
Exemplo de interação:
Adivinhe o número entre 1 e 10: 5
Muito alto, tente novamente!
Adivinhe o número entre 1 e 10: 3
Correto! O número é 3.
"""
import random

n=random.randint(1,10)#gera um numero aleatorio de 1 a 10
x=0
while n != x:
    x=int(input("Adivinhe o número entre 1 e 10: "))
    if x > n:
        print("Muito alto, tente novamente!")
    elif x < n:
        print("Muito baixo, tente novamente!")
    else:
        print("Correto! O número é ",n)
        




