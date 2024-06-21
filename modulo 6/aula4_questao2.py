"""2) Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase
Exemplo:
Digite uma frase: Eu gosto de programar em Python
Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']"""


frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'

lista_vogais = sorted([char for char in frase if char in vogais])
lista_consoantes = [char for char in frase if char.isalpha() and char not in vogais]

print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
