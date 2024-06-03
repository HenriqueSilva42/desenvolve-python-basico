#4) Uma conta poupança foi aberta com um depósito de R$500,00.
# Esta conta é remunerada em 1% de juros ao mês. O código a seguir
# apresenta uma forma de implementação para calcular três meses de 
#acúmulo de juros. Reescreva esse código usando apenas duas variáveis. 

juros = 1.01
saldo = 500.0
saldo = saldo * juros**3

print("Depois de 3 meses o saldo é", saldo)