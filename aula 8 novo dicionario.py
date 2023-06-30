agenda = {}

def menu():
    print("MENU")
    print("================")
    print("1- Adicionar / Excluir")
    print("2- Visualizar agenda")
    print("Escolha:")
    escolha = int(input())
    return escolha

def adicionar_excluir():
    nome = input("Digite o nome: ")
    
    if nome not in agenda:
        telefone = input("Digite o telefone: ")
        agenda[nome] = [telefone]
        print(f"{nome} adicionado com sucesso.")
    else:
        print(f"Nome: {nome}\nTelefones: {', '.join(agenda[nome])}")
        print("1- Adicionar telefone")
        print("2- Excluir nome")
        print("3- Excluir um número")
        opcao = int(input("Escolha: "))
        
        if opcao == 1:
            telefone = input("Digite o novo telefone: ")
            agenda[nome].append(telefone)
            print(f"Telefone {telefone} adicionado com sucesso.")
        elif opcao == 2:
            del agenda[nome]
            print(f"{nome} removido com sucesso.")
        elif opcao == 3:
            telefone = input("Digite o telefone a ser removido: ")
            if telefone in agenda[nome]:
                agenda[nome].remove(telefone)
                print(f"Telefone {telefone} removido com sucesso.")
            else:
                print("Telefone não encontrado.")
        else:
            print("Opção inválida.")

def visualizar_agenda():
    for nome, telefones in agenda.items():
        print(f"Nome: {nome}\nTelefones: {', '.join(telefones)}\n")

while True:
    escolha = menu()
    
    if escolha == 1:
        adicionar_excluir()
    elif escolha == 2:
        visualizar_agenda()
    else:
        print("Opção inválida.")

        
