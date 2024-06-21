# Exemplos de senhas
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

# Pelo menos 8 caracteres de comprimento
if len(senha1) < 8:
    print(False)
else:
    # Pelo menos uma letra maiúscula
    tem_maiuscula = any(c.isupper() for c in senha1)
    if not tem_maiuscula:
        print(False)
    else:
        # Pelo menos uma letra minúscula
        tem_minuscula = any(c.islower() for c in senha1)
        if not tem_minuscula:
            print(False)
        else:
            # Pelo menos um número
            tem_numero = any(c.isdigit() for c in senha1)
            if not tem_numero:
                print(False)
            else:
                # Pelo menos um caractere especial
                caracteres_especiais = set('@#$')
                tem_caracter_especial = any(c in caracteres_especiais for c in senha1)
                if not tem_caracter_especial:
                    print(False)
                else:
                    print(True)

# Saídas esperadas:
# True (para senha1)
# False (para senha2)
# False (para senha3)
