"""
2) Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos.
# Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos,
# armazene em uma lista chamada elementos. Em seguida imprima:
#A lista elementos
#A soma dos valores da lista
#A média dos valores da lista
"""
import random

elementos=[]
num_elementos=random.randint(5,20)

for i in range(num_elementos):
    elementos.append(random.randint(1,10))
    
print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))
