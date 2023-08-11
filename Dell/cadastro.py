import os
import csv


def cadastrar_cliente():
    dados = {}
    
    os.system('cls') or None  #limpa tela
    print("-------------CADASTRAR CLIENTE-------------")

    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu CPF: "))
    rg = int(input("Digite seu RG: "))


    dados[cpf] = {nome, rg}
    
    #print("Cliente: ",dados[cpf], "cadastrado com sucesso!")

    colunas = ["cpf", "nome", "rg"]

    file_exist = os.path.isfile("clientes.csv")
    
    with open('clientes.csv', 'a', newline='', encoding='utf-8') as clientes_csv:
        cadastrar = csv.DictWriter(clientes_csv, fieldnames=colunas, delimiter=";", lineterminator='\r\n')

        if not file_exist:
            cadastrar.writeheader()

        cadastrar.writerow({"cpf":cpf,"nome":nome.title(),"rg":rg})
    print("Cadastrado realizado com sucesso!")


    return 0

def cadastrar_livro():
    livros = {}
    
    nome = input("Nome do livro: ")
    codigo = int(input("Codigo do livro: "))
    autor = input("Autor do livro: ")
    ano_lancamento = input("Ano de lançamento do livro: ")
    

    livros[nome] = {nome, codigo, autor, ano_lancamento}
    colunas = ["nome", "codigo", "autor", "ano de lancamento"]

    file_exist = os.path.isfile("livros.csv")

    with open("livros.csv", "a", newline="", encoding="utf-8") as livros_csv:
        cadastrar = csv.DictWriter(livros_csv, fieldnames=colunas, delimiter=";", lineterminator="\r\n")
        if not file_exist:
            cadastrar.writeheader()

        cadastrar.writerow({"nome":nome.title(), "codigo":codigo, "autor":autor, "ano de lancamento":ano_lancamento })
    print("Cadastro realizado com sucesso!")

    return 0