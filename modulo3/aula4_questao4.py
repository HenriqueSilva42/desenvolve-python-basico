"""
4) Você está implementando um sistema de entrega expressa e precisa
 calcular o valor do frete com base na distância e no peso do pacote.
 Escreva um código que solicita a distância da entrega em quilômetros
   e o peso do pacote em quilogramas.
O programa deve calcular e imprimir o valor do frete de acordo com as
 seguintes regras:
Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
"""

km=float(input("Digite a distância em km é: "))
kg=float(input("Digite o peso em kg é: "))

if km<=100:
    p_por_km=1
elif km>100 and km<=300:
    p_por_km=1.5
elif km>300:
    p_por_km=2
print("O preço do frete é:R$%.2f " % (kg*p_por_km+10 if kg>10 else kg*p_por_km))