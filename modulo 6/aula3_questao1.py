"""
1) Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:
A lista original
Os 3 primeiros elementos
Os 2 últimos elementos
A lista invertida (do fim para o começo)
Os elementos de índice par (0, 2, 4 … )
Os elementos de índice ímpar (1, 3, 5, … )
"""
print("Digite pelo menos 4 números inteiros (digite 'sair' para finalizar):")

lista = []
while True:
    valor = input()
    if valor.lower() == 'sair':
        if len(lista) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números.")
    else:
        try:
            numero = int(valor)
            lista.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Imprimindo a lista original
print("Lista original:", lista)

# Imprimindo os 3 primeiros elementos
print("Os 3 primeiros elementos:", lista[:3])

# Imprimindo os 2 últimos elementos
print("Os 2 últimos elementos:", lista[-2:])

# Imprimindo a lista invertida
print("Lista invertida:", lista[::-1])

# Imprimindo os elementos de índice par
print("Elementos de índice par:", lista[::2])

# Imprimindo os elementos de índice ímpar
print("Elementos de índice ímpar:", lista[1::2])
