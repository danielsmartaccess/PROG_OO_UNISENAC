import os


def is_valid_name(name: str) -> bool:
    return name.isalpha()


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit()


class Pessoa:
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefones = [telefone]

    def get_nome(self):
        return self.__nome

    def get_telefones(self):
        return self.__telefones

    def adicionar_telefone(self, telefone):
        self.__telefones.append(telefone)

    def remover_telefone(self, telefone):
        self.__telefones.remove(telefone)


def encontrar_pessoa(agenda, nome):
    for pessoa in agenda:
        if pessoa.get_nome() == nome:
            return pessoa
    return None


agenda = []

while True:
    cls = os.system('cls' if os.name == 'nt' else 'clear')
    print("MENU")
    print("================")
    print("1- Adicionar / Excluir")
    print("2- Visualizar agenda")
    print(" Escolha:")

    opcao = int(input())

    if opcao == 1:
        nome = input("Digite o nome: ")
        while not is_valid_name(nome):
            print("Nome inválido. Digite novamente: ")
            nome = input()

        pessoa = encontrar_pessoa(agenda, nome)

        if pessoa is None:
            telefone = input("Digite o telefone: ")
            while not is_valid_phone(telefone):
                print("Telefone inválido. Digite novamente: ")
                telefone = input()

            nova_pessoa = Pessoa(nome, telefone)
            agenda.append(nova_pessoa)
            print(f"{nome} adicionado com sucesso.")
        else:
            print(f"Nome: {pessoa.get_nome()}")
            print("Telefones:")
            for telefone in pessoa.get_telefones():
                print(telefone)

            print("\n1- Adicionar outro telefone")
            print("2- Excluir nome")
            print("3- Excluir um número")
            opcao = int(input())

            if opcao == 1:
                telefone = input("Digite o novo telefone: ")
                while not is_valid_phone(telefone):
                    print("Telefone inválido. Digite novamente: ")
                    telefone = input()

                pessoa.adicionar_telefone(telefone)
                print("Telefone adicionado com sucesso.")
            elif opcao == 2:
                agenda.remove(pessoa)
                print("Nome excluído com sucesso.")
            elif opcao == 3:
                telefone = input("Digite o telefone a ser excluído: ")
                while not is_valid_phone(telefone):
                    print("Telefone inválido. Digite novamente: ")
                    telefone = input()

                pessoa.remover_telefone(telefone)
                print("Telefone excluído com sucesso.")
            else:
                print("Opção inválida.")

    elif opcao == 2:
        cls = os.system('cls' if os.name == 'nt' else 'clear')
        print("Agenda:")
        for pessoa in agenda:
            print(f"Nome: {pessoa.get_nome()}")
            print("Telefones:")
            for telefone in pessoa.get_telefones():
                print(telefone)
            print()
        print("Pressione enter para continuar...")
        input()
    else:
        print("Opção inválida.")

