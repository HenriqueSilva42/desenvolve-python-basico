
frase = input("Digite uma frase: ").lower()
vogais = "aeiou"
indices_vogais = []
count = 0

for i, letra in enumerate(frase):
    if letra in vogais:
        count += 1
        indices_vogais.append(i)

print(f"{count} vogais")
print(f"Índices {indices_vogais}")


