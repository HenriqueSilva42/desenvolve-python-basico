#) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura),
#bem como o preço do metro quadrado da região em ponto flutuante.
#Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.
#O terreno possui 250m2 e custa R$512,490.50
#Comente na linha acima de cada instrução uma breve descrição da instrução.
#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2

2

comp,larg,valor=int(input('Qual o comprimento do terreno? : ')),int(input('Qual a largura do terreno?: ')), float(input('Qual o valor do metro quadrado em 00.00?'))
areatotal=comp*larg #calculo largura*comprimento
preçofinal= areatotal*valor #cálculo preço
print(f"O terreno possui {areatotal:,.0f}m2 e custa R${preçofinal:,.2f}")