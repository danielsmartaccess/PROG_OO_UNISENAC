# Classe Pessoa
from tkinter import Menu


class Pessoa:
    # Construtor da classe Pessoa
    def __init__(self, nome, telefone):
        self.__nome = nome  # Atributo privado nome
        self.__telefones = [telefone]  # Atributo privado telefones (inicialmente com um telefone)

    # Método para obter o nome da pessoa
    def get_nome(self):
        return self.__nome

    # Método para obter a lista de telefones da pessoa
    def get_telefones(self):
        return self.__telefones

    # Método para adicionar um telefone à lista de telefones da pessoa
    def adicionar_telefone(self, telefone):
        self.__telefones.append(telefone)

    # Método para remover um telefone da lista de telefones da pessoa
    def remover_telefone(self, telefone):
        self.__telefones.remove(telefone)


# Função para encontrar uma pessoa na agenda pelo nome
def encontrar_pessoa(agenda, nome):
    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            return pessoa
    return None


# Lista que armazena os objetos da classe Pessoa (a agenda)
agenda = []

# Loop principal do menu
def Menu ():

    while True:
        print("MENU")
        print("================")
        print("1- Adicionar / Excluir")
        print("2- Visualizar agenda")
        print(" Escolha:")

        opcao = int(input())  # Lê a opção do usuário

        if opcao == 1:
            nome = input("Digite o nome: ")  # Lê o nome
            pessoa = encontrar_pessoa(agenda, nome)  # Busca a pessoa na agenda pelo nome

            # Se a pessoa não foi encontrada na agenda
            if pessoa is None:
                telefone = input("Digite o telefone: ")  # Lê o telefone
                nova_pessoa = Pessoa(nome, telefone)  # Cria um novo objeto Pessoa
                agenda.append(nova_pessoa)  # Adiciona o objeto Pessoa na lista agenda
                print(f"{nome} adicionado com sucesso.")
            else:
                # Se a pessoa já existe na agenda, mostra as informações
                print(f"Nome: {pessoa.get_nome()}")
                print("Telefones:")
                for telefone in pessoa.get_telefones():
                    print(telefone)

                # Menu de opções para pessoa existente
                print("\n1- Adicionar outro telefone")
                print("2- Excluir nome")
                print("3- Excluir um número")
                opcao = int(input())

                if opcao == 1:
                    telefone = input("Digite o novo telefone: ")
                    pessoa.adicionar_telefone(telefone)
                    print("Telefone adicionado com sucesso.")
                elif opcao == 2:
                    agenda.remove(pessoa)
                    print("Nome excluído com sucesso.")
                elif opcao == 3:
                    telefone = input("Digite o telefone a ser excluído: ")
                    pessoa.remover_telefone(telefone)
                    print("Telefone excluído com sucesso.")
                else:
                    print("Opção inválida.")

        elif opcao == 2:
            # Exibe a agenda
            print("Agenda:")
            for pessoa in agenda:
                print(f"Nome: {pessoa.get_nome()}")
                print("Telefones:")
                for telefone in pessoa.get_telefones():
                    print(telefone)
                print()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    Menu() 