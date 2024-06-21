"""
 Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]
"""
import random

# Gerar a lista de 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Imprimir a lista original
print("Original:", lista)

# Encontrar o intervalo com a maior quantidade de números negativos seguidos
max_negativos_seguidos = 0
inicio_intervalo = 0
fim_intervalo = 0

i = 0
while i < len(lista):
    if lista[i] < 0:
        j = i
        while j < len(lista) and lista[j] < 0:
            j += 1
        qtd_negativos = j - i
        if qtd_negativos > max_negativos_seguidos:
            max_negativos_seguidos = qtd_negativos
            inicio_intervalo = i
            fim_intervalo = j - 1
        i = j
    else:
        i += 1

# Remover o intervalo com a maior quantidade de números negativos seguidos
del lista[inicio_intervalo:fim_intervalo + 1]

# Imprimir a lista após a deleção
print("Editada:", lista)
