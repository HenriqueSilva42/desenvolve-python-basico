
import os
import string

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

arquivo_original = os.path.join(diretorio_atual, "frase.txt")
arquivo_destino = os.path.join(diretorio_atual, "palavras.txt")

def limpar_palavra(palavra):
    return ''.join(filter(str.isalpha, palavra))

with open(arquivo_original, "r") as arquivo:
    texto = arquivo.read()
    palavras = texto.split()

palavras_processadas = [limpar_palavra(palavra).lower() for palavra in palavras]


with open(arquivo_destino, "w") as arquivo:
    arquivo.write("\n".join(palavras_processadas))

print(f"Conteúdo do arquivo '{arquivo_destino}':")
with open(arquivo_destino, "r") as arquivo:
    print(arquivo.read())
