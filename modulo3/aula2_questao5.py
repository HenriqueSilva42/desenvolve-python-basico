"""
5) Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu 
tempo de serviço (em anos) e escreva uma expressão que imprima True
se a pessoa já pode se aposentar, ou False caso contrário, de acordo
com as seguintes regras:
A: Para mulheres, ter mais de 60 anos. Para homens, 65.
B: Ou ter trabalhado pelo menos 30 anos
C: Ou ter 60 anos  e trabalhado pelo menos 25.
"""

gênero= (input("Gênero M ou F? "))
idade=int(input("Idade em anos: "))
tempo_serviço=int(input("Tempo de serviço em anos: "))

A = (gênero == 'F' and idade >= 60) or \
    (gênero == 'M' and idade >= 65) 

A = tempo_serviço>30 

C = idade== 60 and tempo_serviço >= 25
Aposenta= A or B or C
print(Aposenta)