while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break #para a função break
    
    # Remover espaços em branco e pontuação e colocar tudo em minúsculas
    frase_tratada = ''.join(e for e in frase if e.isalnum()).lower()
    if frase_tratada == frase_tratada[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
