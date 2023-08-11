import csv
import os 


def pesquisar_cliente(nome_cliente):

    clientes_csv = open('clientes.csv') 
    dados_cliente = csv.DictReader(clientes_csv, delimiter=';')

    for cliente in dados_cliente:
        if(cliente["nome"].lower() == nome_cliente.lower()):
            nome = (cliente['nome'])
            cpf = (cliente['cpf'])
            x = (True, cpf, nome)
            return x
            break       
        return (False, )




def pesquisar_livro(codigo_livro):
    
    livros_csv = open('livros.csv') 
    dados_livros = csv.DictReader(livros_csv, delimiter=';')

    for livro in dados_livros:
        if(livro["codigo"] == codigo_livro):
            nome = (livro['nome'])
            autor = (livro['autor'])
            ano_lanc = (livro['ano de lancamento'])  
            x = (True, codigo_livro, nome, autor, ano_lanc)        
            return x
            break
        else:
            return (False,)
   

        

