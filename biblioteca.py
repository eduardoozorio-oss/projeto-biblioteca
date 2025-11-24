biblioteca = {
    1: {"titulo": "Python Básico", "autor": "Gabriel", "disponivel": True},
    2: {"titulo": "Lógica de Programação", "autor": "Valdinei", "disponivel": False},
    3: {"titulo": "Algoritmos", "autor": "James", "disponivel": True}
}


# CONSULTAR
def consultar_livro():
    while True:
        try:
            id = int(input("ID do livro que deseja consultar: "))
            print("Livro encontrado:", biblioteca[id])
            break
        except KeyError:
            print("Esse ID não existe. Tente novamente.")
        except ValueError:
            print("Digite apenas números.")
        finally:
            print("Operação finalizada.\n")


# ADICIONAR
def adicionar_livro():
    while True:
        try:
            id = int(input("ID do novo livro: "))

            if id in biblioteca:
                raise KeyError

            titulo = input("Título: ")
            autor = input("Autor: ")

            biblioteca[id] = {"titulo": titulo, "autor": autor, "disponivel": True}
            print("Livro adicionado!")
            break

        except KeyError:
            print("Já existe um livro com esse ID.")
        except ValueError:
            print("ID precisa ser um número.")
        finally:
            print("Operação finalizada.\n")
