"""
1) Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e
os armazene em uma lista. Em seguida imprima na #ordem estabelecida:
A lista ordenada, sem modificar a lista original
A lista original
O índice do maior valor da lista
O índice do menor valor da lista
"""
import random

lista=[]

for i in range(21):
    lista.append(random.randint(-100,100))


lista_ordenada = sorted(lista)
    
print("Lista ordenada (sem modificar a lista original):")
print(lista_ordenada)
    
print("\nLista original:")
print(lista)
    
indice_maior_valor = lista.index(max(lista))
indice_menor_valor = lista.index(min(lista))
    
print(f"\nÍndice do maior valor da lista: {indice_maior_valor}")
print(f"Índice do menor valor da lista: {indice_menor_valor}")

