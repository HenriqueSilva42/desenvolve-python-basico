"""4) Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
#Exemplo de interação via terminal (entradas em negrito):
#Digite a quantidade de elementos da lista 1: 4
#Digite os 4 elementos da lista 1:
#1
#2
#3
#4Digite a quantidade de elementos da lista 2: 6
#Digite os 6 elementos da lista 2:
#5
#6
#7
#8
#9
#10Lista intercalada: 1 5 2 6 3 7 4 8 9 10
"""
# Solicita a quantidade de elementos da lista 1
qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
lista2 = []

# Solicita os elementos da lista 1
print(f"Digite os {qtd1} elementos da lista 1:")
for i in range(qtd1):
    item = int(input())
    lista1.append(item)

# Solicita a quantidade de elementos da lista 2
qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
# Solicita os elementos da lista 2
print(f"Digite os {qtd2} elementos da lista 2:")
for i in range(qtd2):
    item = int(input())
    lista2.append(item)

# Cria a lista intercalada
lista3 = []

# Intercala os elementos das duas listas
min_len = min(qtd1, qtd2)
for i in range(min_len):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

# Adiciona os elementos restantes da lista maior
if qtd1 > qtd2:
    lista3.extend(lista1[min_len:])
else:
    lista3.extend(lista2[min_len:])

# Exibe a lista intercalada
print("Lista intercalada:", ' '.join(map(str, lista3)))

    