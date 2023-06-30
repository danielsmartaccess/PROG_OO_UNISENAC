"""Dicionario é uma estrutura de dados que armazena pares de chave e valor.

Utilizando o menu a baixo crie uma agenda usando dicionario e armazene
    os objetos de Pessoa criados em uma lista.
    agenda = {Pessoa1: [telefone1, telefone2, ...],}

MENU
================
1- Adicionar / Excluir
2- Visualizar agenda
 Escolha:


Descrição:
Na opção 1: Ler nome
                Caso nome não exista na agenda, ler telefone, Instanciar e
                adicionar em agenda.
            Caso o nome já exista, mostre os dados. Perguntar se quer
                adicionar outro telefone, ou se quer
                excluir o nome localizado, ou excluir um número.

Na opção 2: mostrar na tela o nome e os telefones das pessoas."""
    
agenda = {}

def adicionar():
    nome = input("Digite o nome: ")
    if nome not in agenda:
        telefone = input("Digite o telefone: ")
        agenda[nome] = [telefone]
    else:
        print("Nome já existe na agenda.")
        print(agenda[nome])
        opcao = input("Deseja adicionar mais um telefone? (S/N) ").upper()
        if opcao == "S":
            telefone = input("Digite o telefone: ")
            agenda[nome].append[telefone]
        else:
            opcao = input("Deseja excluir o nome? (S/N) ").upper()
            if opcao == "S":
                del agenda[nome]
            else:
                opcao = input("Deseja excluir um telefone? (S/N) ").upper()
                if opcao == "S":
                    telefone = input("Digite o telefone: ")
                    agenda[nome].remove[telefone]


def visualizar():
    for nome, telefones in agenda.items():
        print(nome, telefones)


def main():
    while True:
        print("MENU")
        print("1- Adicionar / Excluir")
        print("2- Visualizar agenda")
        print("3- Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            visualizar()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")
        print("================")


if __name__ == "__main__":
    main()








