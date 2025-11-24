def menu():
    while True:
        print("1 - Consultar")
        print("2 - Adicionar")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("5 - Sair")

        op = input("Escolha: ")

        if op == "1":
            consultar_livro()
        elif op == "2":
            adicionar_livro()
        elif op == "3":
            atualizar_livro()
        elif op == "4":
            deletar_livro()
        elif op == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

menu()
