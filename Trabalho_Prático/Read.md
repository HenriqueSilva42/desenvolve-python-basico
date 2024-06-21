# Sistema de Gerenciamento TechStore

## Introdução
A "TechStore" é uma empresa fictícia que vende produtos de tecnologia como laptops, smartphones e tablets. Este sistema permite que diferentes tipos de usuários (administrador, vendedor, cliente) gerenciem e visualizem informações de produtos e usuários de acordo com suas permissões.

## Implementação

### Usuários

#### Estrutura de Dados
A estrutura de dados para os usuários é um dicionário Python, onde cada chave é o nome de usuário e o valor é outro dicionário contendo senha e permissão.

#### Arquivo de Registro
Os dados dos usuários são armazenados no arquivo `usuarios.csv`, com as colunas `username`, `senha`, `permissao`.

#### Funcionalidades CRUD

- **Create:** `criar_usuario(username, senha, permissao)`
- **Read:** `listar_usuarios()`
- **Update:** `atualizar_usuario(username, nova_senha, nova_permissao)`
- **Delete:** `deletar_usuario(username)`

### Produtos

#### Estrutura de Dados
A estrutura de dados para os produtos é uma lista de dicionários, onde cada dicionário representa um produto com atributos como código, nome, preço e quantidade.

#### Arquivo de Registro
Os dados dos produtos são armazenados no arquivo `produtos.csv`, com as colunas `codigo`, `nome`, `preco`, `quantidade`.

#### Funcionalidades CRUD

- **Create:** `criar_produto(codigo, nome, preco, quantidade)`
- **Read:** `listar_produtos()`
- **Update:** `atualizar_produto(codigo, novo_nome, novo_preco, nova_quantidade)`
- **Delete:** `deletar_produto(codigo)`

#### Funcionalidades Adicionais

- **Buscar Produto por Nome:** `buscar_produto_por_nome(nome)`
- **Ordenar Produtos por Nome:** `ordenar_produtos_por_nome()`
- **Ordenar Produtos por Preço:** `ordenar
