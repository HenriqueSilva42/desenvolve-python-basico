def contar_caracteres(palavra):
    char_count = {}
    for char in palavra:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def encontrar_anagramas():
    frase = input("Digite uma frase: ").lower()
    palavra_objetivo = input("Digite a palavra objetivo: ").lower()

    palavras_frase = frase.split()
    objetivo_count = contar_caracteres(palavra_objetivo)
    anagramas = []

    for palavra in palavras_frase:
        if len(palavra) == len(palavra_objetivo) and contar_caracteres(palavra) == objetivo_count:
            anagramas.append(palavra)

    print(f"Anagramas: {anagramas}")

encontrar_anagramas()
