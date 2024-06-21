import os
import re

def contar_mencoes_personagens(nome_arquivo):
    # Definindo os nomes dos personagens e suas variações
    nomes_personagens = ['Nonato', 'Íria']

    # Inicializando variáveis para armazenar resultados
    primeira_25_linhas = []
    numero_linhas = 0
    linha_mais_longa = ''
    tamanho_mais_longa = 0
    mencoes_nonato = 0
    mencoes_iria = 0

    # Obtendo o caminho absoluto do diretório atual do script
    diretorio_script = os.path.dirname(os.path.abspath(__file__))

    # Caminho completo para o arquivo estomago.txt
    caminho_arquivo = os.path.join(diretorio_script, nome_arquivo)

    # Verificando se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado no diretório do script.")
        return

    # Tentando abrir o arquivo com diferentes codificações
    codificacoes = ['utf-8', 'latin-1']
    for codificacao in codificacoes:
        try:
            with open(caminho_arquivo, 'r', encoding=codificacao) as arquivo:
                # Lendo as primeiras 25 linhas
                for i in range(25):
                    linha = arquivo.readline().strip()
                    primeira_25_linhas.append(linha)

                    # Verificando a linha com maior número de caracteres
                    if len(linha) > tamanho_mais_longa:
                        tamanho_mais_longa = len(linha)
                        linha_mais_longa = linha

                    # Contando menções aos nomes dos personagens
                    for nome in nomes_personagens:
                        mencoes = len(re.findall(rf'\b{re.escape(nome)}\b', linha, re.IGNORECASE))
                        if nome == 'Nonato':
                            mencoes_nonato += mencoes
                        elif nome == 'Íria':
                            mencoes_iria += mencoes

                # Contando o número total de linhas
                arquivo.seek(0)
                numero_linhas = sum(1 for linha in arquivo)

                # Encerra o loop se conseguir abrir sem erros
                break

        except UnicodeDecodeError:
            # Se houver erro de decodificação, tenta a próxima codificação
            continue

    # Exibindo resultados
    print("Texto das primeiras 25 linhas:")
    for linha in primeira_25_linhas:
        print(linha)

    print(f"\nNúmero total de linhas no arquivo: {numero_linhas}")
    print(f"\nLinha com maior número de caracteres:")
    print(linha_mais_longa)
    print(f"\nNúmero de menções ao personagem 'Nonato': {mencoes_nonato}")
    print(f"Número de menções ao personagem 'Íria': {mencoes_iria}")

# Chamando a função com o nome do arquivo 'estomago.txt'
contar_mencoes_personagens('estomago.txt')
