import cadastro
import listar
import remover
import emprestimo

resposta = "s"

while resposta == "s":
    menu = '''===================================================
    \r====[1] Cadastrar cliente                     =====
    \r====[2] Cadastrar livro                       =====
    \r====[3] Realizar Emprestimo                   =====
    \r====[4] Listar livro                          =====   
    \r====[5] Listar clientes                       =====
    \r====[6] Listar emprestimos                    =====
    \r====[7] Remover cliente                       =====
    \r====[8] Remover livro                         =====
    \r====[9] Sair                                  =====
    \r==================================================='''                                  

    print(menu)

    opcao = int(input("Escolha uma opçao: "))

    if opcao == 1:
        cadastro.cadastrar_cliente()
    elif opcao == 2:
        cadastro.cadastrar_livro()
    elif opcao == 3:
        emprestimo.emprestar_livro()
    elif opcao == 4:
        listar.listar_livro()
    elif opcao == 5:
        listar.listar_cliente()
    elif opcao == 6:
        listar.listar_emprestimo()
    elif opcao == 7:
        remover.remover_cliente()
    elif opcao == 8:
        remover.remover_livro()
    elif opcao == 9:
        exit
        break
    else:
        print("Digite uma opçao valida!")

    resposta = input("Deseja continuar? [s/n]")
    