import random

def escolhe_palavra():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
        palavras = f.readlines()
    return random.choice(palavras).strip().lower()

def imprime_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def imprime_enforcado(erros):
    desenhos = [
        "|---|\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "   |\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "   |\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "  /|\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "  /|\\\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "  /|\\\n"
        "   |\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "  /|\\\n"
        "  /\n"
        "=========",
        
        "|---|\n"
        "   O\n"
        "  /|\\\n"
        "  / \\\n"
        "========="
    ]
    
    print(desenhos[erros])

def jogo_da_forca():
    palavra = escolhe_palavra()
    letras_corretas = set()
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta. Ela tem", len(palavra), "letras.")
    print(imprime_palavra(palavra, letras_corretas))

    while tentativas > 0:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra:
            letras_corretas.add(letra)
            print("Letra correta!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra errada!")
            imprime_enforcado(6 - tentativas)
        
        print(imprime_palavra(palavra, letras_corretas))

        if all(letra in letras_corretas for letra in palavra):
            print("Parabéns! Você acertou a palavra:", palavra)
            break

    if tentativas == 0:
        print("Você foi enforcado! A palavra era:", palavra)

# Rodando o jogo
jogo_da_forca()
