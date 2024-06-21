"""
Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e 
#calcule a diferença absoluta entre esses dois números.
#Utilize a função nativa abs para garantir que o resultado seja sempre positivo
#e round para arredondar o resultado para duas casas decimais.
"""

n1=float(input("Digite o primeiro número:"))
n2=float(input("Digite o segundo número:"))
difer=abs(n1-n2)
difer=round(difer,2)

print("A diferença absoluta arredondada entre os números é:", difer)