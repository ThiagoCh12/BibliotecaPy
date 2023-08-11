import os
import csv
import pesquisar

def listar_cliente():
    os.system('cls') or None
    print("====LISTAGEM DE CLIENTES====")
    clientes_csv = open("clientes.csv")
    dados_clientes = csv.DictReader(clientes_csv, delimiter=';')

    for clientes in dados_clientes:
        print(clientes)
    

def listar_livro():

    os.system('cls') or None
    print("====LISTAGEM DE LIVROS====")
    livros_csv = open("livros.csv")
    dados_livros = csv.DictReader(livros_csv, delimiter=';')

    for livros in dados_livros:
        print(livros)

def listar_emprestimo():

    os.system('cls') or None
    print("====LISTAGEM DE EMPRESTIMOS====")
    emprestimo_csv = open("emprestimo.csv")
    dados_emprestimos = csv.DictReader(emprestimo_csv, delimiter=';')

    for emprestimos in dados_emprestimos:
        print(emprestimos)


def listar_atrasos():
    

    return 0