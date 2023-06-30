lista_nomes = []
lista_matriculas = []

def ler_nome():
    nome = input("Digite o nome do aluno: ")
    while len(nome) < 3 or any(char.isdigit() for char in nome):
        print("Nome inválido! O nome deve ter no mínimo 3 caracteres e não pode conter números.")
        nome = input("Digite novamente o nome do aluno: ")
    return nome


def ler_matricula():
    """
    Lê a matrícula de um aluno.
    """
    matricula = input("Digite a matrícula do aluno: ")
    # Verifica se a matrícula contém apenas dígitos numéricos
    if not matricula.isdigit():
        print("A matrícula deve conter apenas dígitos numéricos.")
        return ler_matricula()  # Chama a função recursivamente em caso de erro
    return matricula


def adiciona_nome(nome):
    """
    Adiciona um nome na lista de nomes.
    """
    lista_nomes.append(nome)
    return lista_nomes


def adiciona_matricula(matricula):
    """
    Adiciona uma matrícula na lista de matrículas.
    """
    lista_matriculas.append(matricula)
    return lista_matriculas

def imprimir_lista_alunos(nomes, matriculas):
    """
    Imprime duas listas, uma contendo os nomes dos alunos e outra contendo suas matrículas, em formato de tabela.
    """
    print("{:<10} {}".format("Aluno", "Matrícula"))
    for nome, matricula in zip(nomes, matriculas):
        print("{:<10} {}".format(nome, matricula))
        
        
def inicio():
    while True:
        escolha = input('''
        Menu
        ====================
        1- Adicionar nome
        2- imprimir dados
        ====================
        Escolha: ''')

        if escolha == "1":
            adicionar_dados()
        elif escolha == '2':
            imprimir_dados()
        else:
            print("Opção inválida! Tente novamente.")

def adicionar_dados():
    adiciona_nome(ler_nome())
    adiciona_matricula(ler_matricula())

def imprimir_dados():
    lista_nomes = retorna_lista_nomes()
    lista_matriculas = retorna_lista_matriculas()
    imprimir_lista_alunos(lista_nomes, lista_matriculas)

inicio()
while True:
    nome = ler_nome()
    matricula = ler_matricula()
    adiciona_nome(nome)
    adiciona_matricula(matricula)
    resp = input("Deseja continuar? [S/N] ")
    if resp in "Nn":
        imprimir_lista_alunos(lista_nomes, lista_matriculas)
        break
    else:
        #print("Opção inválida! Tente novamente.")
        continue

 