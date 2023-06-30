#Crie uma classe Aluno com os seguintes
# atributos de instância:
# - nome
# - matricula
# - data_nascimento
#
# Crie uma lista com instâncias desta classe
#   - crie uma função para adicionar alunos na lista
#   - crie uma função para verificar se um aluno existe
#       ou não na lista. Esta função deve retornar os
#       dados de aluno, mas caso o aluno não conste na
#       lista, retorne a mensagem "ALUNO NÃO MATRICULADO"
#       > consulte pela matrícula ou nome
#   - crie uma função para mostrar todos os alunos da
#       lista, com nome e matricula.


class Aluno:
    def __init__(self, nome, matricula, data_nascimento):
        self.nome = nome
        self.matricula = matricula
        self.data_nascimento = data_nascimento

class ListaAlunos:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def verificar_aluno(self, consulta):
        for aluno in self.alunos:
            if consulta == aluno.nome or consulta == aluno.matricula:
                return f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}, Data de Nascimento: {aluno.data_nascimento}"
        return "ALUNO NÃO MATRICULADO"

    def mostrar_todos_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}")

# Criando instâncias da classe Aluno
aluno1 = Aluno("João Silva", "001", "01/01/2000")
aluno2 = Aluno("Maria Souza", "002", "02/02/2001")
aluno3 = Aluno("Carlos Pereira", "003", "03/03/2002")

# Criando instância da classe ListaAlunos
lista_alunos = ListaAlunos()

# Adicionando alunos à lista
lista_alunos.adicionar_aluno(aluno1)
lista_alunos.adicionar_aluno(aluno2)
lista_alunos.adicionar_aluno(aluno3)

# Verificando se um aluno existe na lista
consulta1 = lista_alunos.verificar_aluno("Maria Souza")
consulta2 = lista_alunos.verificar_aluno("004")

print(consulta1)  # Saída: Nome: Maria Souza, Matrícula: 002, Data de Nascimento: 02/02/2001
print(consulta2)  # Saída: ALUNO NÃO MATRICULADO

# Mostrando todos os alunos da lista
lista_alunos.mostrar_todos_alunos()
# Saída:
# Nome: João Silva, Matrícula: 001
# Nome: Maria Souza, Matrícula: 002
# Nome: Carlos Pereira, Matrícula: 003

