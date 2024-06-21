""""
Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e
calcule a raíz quadrada da soma dos valores.
Peça ao usuário o valor de n
Biblioteca random: Função randint()
Biblioteca math: Função sqrt()
"""
import random
import math

n = int(input("Digite o valor de n: "))

soma = sum(random.randint(0, 100) for _ in range(n))#sum() soma randint(x,y) gera um valor entre 0 e 100 
raiz = math.sqrt(soma)

print(f"Soma dos valores: {soma}")
print(f"Raiz quadrada da soma: {raiz:.2f}")




