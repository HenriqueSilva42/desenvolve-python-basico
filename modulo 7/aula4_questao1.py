# Exercício 1: Salvar frase digitada pelo usuário em um arquivo na mesma pasta do script

import os

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Obtém o diretório onde o script está localizado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Caminho completo do arquivo a ser salvo
caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

# Salva a frase no arquivo
with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_arquivo}")
a