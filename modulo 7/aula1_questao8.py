def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_1 = 0
    else:
        digito_verif_1 = 11 - resto

    # Verifica o primeiro dígito verificador
    if digito_verif_1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verif_2 = 0
    else:
        digito_verif_2 = 11 - resto

    # Verifica o segundo dígito verificador
    if digito_verif_2 != int(cpf[10]):
        return False

    # CPF válido se passou por todas as verificações
    return True


cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

if validar_cpf(cpf):
        print("CPF Válido")
else:
        print("CPF Inválido")


