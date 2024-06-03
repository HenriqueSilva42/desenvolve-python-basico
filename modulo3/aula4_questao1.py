#1) Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar.
# Critério: se o resto da divisão do número por 2 for 0, o número é par, caso contrário é ímpar.
# Lembre-se do operador do python % que retorna o resto de uma divisão.

n1=int(input("Informe um número: "))
n2=int(input("Informe outro número: "))
print(
    "A soma é par" if ((numero1+numero2)%2==0) 
      else "A soma é ímpar")