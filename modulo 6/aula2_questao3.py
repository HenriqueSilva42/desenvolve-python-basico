import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Calcular a interseção das duas listas sem duplicatas
interseccao = list(set(lista1) & set(lista2))
interseccao_ordenada = sorted(interseccao)

# Contar a frequência de cada elemento em cada lista
contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

# Imprimir as listas e a interseção ordenada
print("lista1 -", lista1)
print("lista2 -", lista2)
print("Interseccao -", interseccao_ordenada)

# Imprimir a contagem de cada elemento da interseção em ambas as listas
print("Contagem")
for elemento in interseccao_ordenada:
    print(f"{elemento}: (lista1={contagem_lista1[elemento]}, lista2={contagem_lista2[elemento]})")
