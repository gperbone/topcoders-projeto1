import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    lista_de_categorias = []
    
    for item in dados:
        if item["categoria"] not in lista_de_categorias:
            lista_de_categorias.append(item["categoria"])
    
    return lista_de_categorias

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_categoria = []
    for item in dados:
        if item["categoria"] == categoria:
            lista_categoria.append(item)

    return lista_categoria
    

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_categoria = listar_por_categoria(dados, categoria)
    lista_ordenada_mais_caro = sorted(lista_categoria, key=lambda x: float(x["preco"]), reverse=True)

    return lista_ordenada_mais_caro[0]


def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_categoria = listar_por_categoria(dados, categoria)
    lista_ordenada_mais_barato = sorted(lista_categoria, key=lambda x: float(x["preco"]))

    return lista_ordenada_mais_barato[0]

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_top_10_caros = sorted(dados, key=lambda x: float(x["preco"]), reverse=True)
    return lista_top_10_caros[0:10]

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    lista_top_10_baratos = sorted(dados, key=lambda x: float(x["preco"]))
    return lista_top_10_baratos[0:10]

def menu(dados):
    ativo = 1

    while ativo == 1:
        print('''
::: LISTA DE OPÇÕES :::
[1] Listar categorias
[2] Listar produtos de uma categoria
[3] Produto mais caro por categoria
[4] Produto mais barato por categoria
[5] Top 10 produtos mais caros
[6] Top 10 produtos mais baratos
[0] Sair
        ''')

        opt = input("Digite a opção desejada: ")

        while not(opt.isdigit()):
            opt = input("Digite apenas números! Digite a opção desejada: ")

        opt = int(opt)

        if opt == 1:
            lista = listar_categorias(dados)

            print("As categorias disponíveis são:")
            j = 0
            for i in range (0,len(lista)):
                print(lista[i], end="")
                if j != 3:
                    print(" | ", end = "")
                    j += 1
                if j == 3:
                    print()
                    j = 0

            ativo = 1
        elif opt == 2:
            cat = input("Digite a categoria desejada: ")
            resultado = listar_por_categoria(dados, cat)
            for item in resultado:
                print(f"{item['id']} | {item['categoria']} | {item['preco']}")

            ativo = 1
        elif opt == 3:
            cat = input("Digite a categoria desejada: ")
            mais_caro_cat = produto_mais_caro(dados, cat)

            print(f"O produto mais caro na categoria {cat} é:\n{mais_caro_cat['id']} | R${mais_caro_cat['preco']}")
            ativo = 1
        elif opt == 4:
            cat = input("Digite a categoria desejada: ")
            mais_barato_cat = produto_mais_barato(dados, cat)

            print(f"O produto mais barato na categoria {cat} é:\n{mais_barato_cat['id']} | R${mais_barato_cat['preco']}")

            ativo = 1
        elif opt == 5:    
            lista_top = top_10_caros(dados)   

            print("--- TOP 10 PRODUTOS MAIS CAROS ---")
            for item in lista_top:
                print(f"R$ {item['preco']} | {item['id']} | {item['categoria']}")

            ativo = 1
        elif opt == 6:
            lista_top = top_10_baratos(dados)

            print("--- TOP 10 PRODUTOS MAIS BARATOS ---")
            for item in lista_top:
                print(f"R$ {item['preco']} | {item['id']} | {item['categoria']}")

            ativo = 0
        elif opt == 0:
            print("Até mais!")
            return False
        else: 
            print("Opção inválida. Tente novamente.")
            ativo = 1



# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)