import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)
    nomes_cript = []

    for nome in nomes:
        nome_cript = ''
        for char in nome:
            novo_char = chr(ord(char) + chave_aleatoria)
            if ord(novo_char) > 126:  # Verifica se ultrapassou o limite ASCII visível
                novo_char = chr(ord(novo_char) - 94)
            nome_cript += novo_char
        nomes_cript.append(nome_cript)

    return nomes_cript, chave_aleatoria

# Exemplo de uso
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)
print(f"Nomes criptografados: {nomes_cript}")
print(f"Chave de criptografia: {chave}")
