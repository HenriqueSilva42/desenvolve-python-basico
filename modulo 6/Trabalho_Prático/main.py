
import csv

usuarios = {
    'admin': {'senha': 'admin123', 'permissao': 'admin'},
    'vendedor1': {'senha': 'vendedor123', 'permissao': 'vendedor'},
    'cliente1': {'senha': 'cliente123', 'permissao': 'cliente'}
}

produtos = [
    {'codigo': 'P001', 'nome': 'Laptop', 'preco': 1500.0, 'quantidade': 10},
    {'codigo': 'P002', 'nome': 'Smartphone', 'preco': 800.0, 'quantidade': 20}
]




def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios[row['username']] = {'senha': row['senha'], 'permissao': row['permissao']}
    return usuarios

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'senha', 'permissao'])
        for username, info in usuarios.items():
            writer.writerow([username, info['senha'], info['permissao']])

def carregar_produtos():
    produtos = []
    with open('produtos.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos.append({'codigo': row['codigo'], 'nome': row['nome'], 'preco': float(row['preco']), 'quantidade': int(row['quantidade'])})
    return produtos

def salvar_produtos(produtos):
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['codigo', 'nome', 'preco', 'quantidade'])
        for produto in produtos:
            writer.writerow([produto['codigo'], produto['nome'], produto['preco'], produto['quantidade']])

def criar_usuario(username, senha, permissao):
    if username in usuarios:
        print("Usuário já existe!")
    else:
        usuarios[username] = {'senha': senha, 'permissao': permissao}
        salvar_usuarios(usuarios)
        print("Usuário criado com sucesso!")

def listar_usuarios():
    for username, info in usuarios.items():
        print(f"Username: {username}, Permissão: {info['permissao']}")

def atualizar_usuario(username, nova_senha, nova_permissao):
    if username in usuarios:
        usuarios[username] = {'senha': nova_senha, 'permissao': nova_permissao}
        salvar_usuarios(usuarios)
        print("Usuário atualizado com sucesso!")
    else:
        print("Usuário não encontrado!")

def deletar_usuario(username):
    if username in usuarios:
        del usuarios[username]
        salvar_usuarios(usuarios)
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado!")

def criar_produto(codigo, nome, preco, quantidade):
    produto = {'codigo': codigo, 'nome': nome, 'preco': preco, 'quantidade': quantidade}
    produtos.append(produto)
    salvar_produtos(produtos)
    print("Produto criado com sucesso!")

def listar_produtos():
    for produto in produtos:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def atualizar_produto(codigo, novo_nome, novo_preco, nova_quantidade):
    for produto in produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = novo_nome
            produto['preco'] = novo_preco
            produto['quantidade'] = nova_quantidade
            salvar_produtos(produtos)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado!")

def deletar_produto(codigo):
    global produtos
    produtos = [produto for produto in produtos if produto['codigo'] != codigo]
    salvar_produtos(produtos)
    print("Produto removido com sucesso!")

def buscar_produto_por_nome(nome):
    for produto in produtos:
        if produto['nome'].lower() == nome.lower():
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
            return
    print("Produto não encontrado!")

def ordenar_produtos_por_nome():
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def ordenar_produtos_por_preco():
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])
    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")


#######################################

def main():
    global usuarios
    global produtos

    usuarios = carregar_usuarios()
    produtos = carregar_produtos()

    # Menu de exemplo (somente para fins de demonstração)
    while True:
        print("\n1. Gerenciar Usuários\n2. Gerenciar Produtos\n3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n1. Criar Usuário\n2. Listar Usuários\n3. Atualizar Usuário\n4. Deletar Usuário")
            opcao_usuarios = input("Escolha uma opção: ")

            if opcao_usuarios == '1':
                username = input("Username: ")
                senha = input("Senha: ")
                permissao = input("Permissão: ")
                criar_usuario(username, senha, permissao)

            elif opcao_usuarios == '2':
                listar_usuarios()

            elif opcao_usuarios == '3':
                username = input("Username: ")
                nova_senha = input("Nova Senha: ")
                nova_permissao = input("Nova Permissão: ")
                atualizar_usuario(username, nova_senha, nova_permissao)

            elif opcao_usuarios == '4':
                username = input("Username: ")
                deletar_usuario(username)

        elif opcao == '2':
            print("\n1. Criar Produto\n2. Listar Produtos\n3. Atualizar Produto\n4. Deletar Produto\n5. Buscar Produto por Nome\n6. Ordenar Produtos por Nome\n7. Ordenar Produtos por Preço")
            opcao_produtos = input("Escolha uma opção: ")

            if opcao_produtos == '1':
                codigo = input("Código: ")
                nome = input("Nome: ")
                preco = float(input("Preço: "))
                quantidade = int(input("Quantidade: "))
                criar_produto(codigo, nome, preco, quantidade)

            elif opcao_produtos == '2':
                listar_produtos()

            elif opcao_produtos == '3':
                codigo = input("Código: ")
                novo_nome = input("Novo Nome: ")
                novo_preco = float(input("Novo Preço: "))
                nova_quantidade = int(input("Nova Quantidade: "))
                atualizar_produto(codigo, novo_nome, novo_preco, nova_quantidade)

            elif opcao_produtos == '4':
                codigo = input("Código: ")
                deletar_produto(codigo)

            elif opcao_produtos == '5':
                nome = input("Nome: ")
                buscar_produto_por_nome(nome)

            elif opcao_produtos == '6':
                ordenar_produtos_por_nome()

            elif opcao_produtos == '7':
                ordenar_produtos_por_preco()

        elif opcao == '3':
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
