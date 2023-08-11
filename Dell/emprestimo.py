import os
import csv
import pesquisar as p
from datetime import date

def emprestar_livro():
    
    nome_cliente = input("Digite o nome do usuario: ")
    retorno_usuario = (p.pesquisar_cliente(nome_cliente))
    
    
    if retorno_usuario[0] == True:
        codigo_livro = input("Digite o codigo do livro:")
        retorno_livro = p.pesquisar_livro(codigo_livro)

        if retorno_livro[0] != True:
            
            print("Nao existe")
        else:

            print('nome do livro:', retorno_livro[1])
            r = input("Deseja emprestar o livro {} para {}? s/n".format(retorno_livro[0], nome_cliente))
            if r == 's':
                data_emprestimo = date.today()

            colunas = ["cpf", 'nome_usuario', 'codigo_livro', 'titulo_livro', 'data_emprestimo']
            files_exists = os.path.isfile("emprestimos.csv")

            with open("emprestimo.csv", "a",newline='', encoding='utf-8') as emprestimo_csv:
                cadastrar = csv.DictWriter(emprestimo_csv, fieldnames= colunas, delimiter=';', lineterminator='\r\n')
                if not files_exists:    
                    cadastrar.writeheader()
                cadastrar.writerow({'cpf': retorno_usuario[1], 'nome_usuario': retorno_usuario[2], 'codigo_livro':codigo_livro,
                                     'titulo_livro':retorno_livro[2], 'data_emprestimo': data_emprestimo})
        
            print("Concluido")
    return (False,)

