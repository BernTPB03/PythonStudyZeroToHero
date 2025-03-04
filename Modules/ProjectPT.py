import os

produtos = []


def exibir_cabecalho():
    print("=====================================")
    print("     Lista de Compras Simples       ")
    print("=====================================")


def adicionar_produto():
    print("\nAdicionando um novo produto:")
    nome = input("Nome do produto: ")
    unidade = input(
        "Unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ").capitalize()
    while unidade not in ['Quilograma', 'Grama', 'Litro', 'Mililitro', 'Unidade', 'Metro', 'Centímetro']:
        print("Unidade inválida! Tente novamente.")
        unidade = input(
            "Unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ").capitalize()

    try:
        quantidade = float(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida! A quantidade deve ser um número.")
        return

    descricao = input("Descrição do produto: ")
    id_produto = len(produtos) + 1
    produto = {
        "id": id_produto,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    }
    produtos.append(produto)
    print(f"\nProduto '{nome}' adicionado com sucesso!")


def remover_produto():
    try:
        id_produto = int(input("\nDigite o ID do produto a ser removido: "))
        produto_removido = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_removido = produto
                produtos.remove(produto)
                break
        if produto_removido:
            print(f"\nProduto '{produto_removido['nome']}' removido com sucesso!")
        else:
            print("\nProduto não encontrado com esse ID.")
    except ValueError:
        print("\nID inválido! Tente novamente.")


def pesquisar_produtos():
    nome_pesquisa = input("\nDigite o nome ou parte do nome do produto: ").lower()
    resultados = [produto for produto in produtos if nome_pesquisa in produto['nome'].lower()]
    if resultados:
        print(f"\n{len(resultados)} produto(s) encontrado(s):")
        for produto in resultados:
            print(
                f"ID: {produto['id']} - Nome: {produto['nome']} - Quantidade: {produto['quantidade']} {produto['unidade']} - Descrição: {produto['descricao']}")
    else:
        print("\nNenhum produto encontrado.")


def listar_produtos():
    if produtos:
        print("\nProdutos na lista de compras:")
        for produto in produtos:
            print(
                f"ID: {produto['id']} - Nome: {produto['nome']} - Quantidade: {produto['quantidade']} {produto['unidade']} - Descrição: {produto['descricao']}")
    else:
        print("\nNenhum produto na lista.")


def menu():
    while True:
        exibir_cabecalho()
        listar_produtos()
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produtos")
        print("4. Sair")

        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            remover_produto()
        elif escolha == "3":
            pesquisar_produtos()
        elif escolha == "4":
            print("\nSaindo do programa... Até logo!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")


menu()
