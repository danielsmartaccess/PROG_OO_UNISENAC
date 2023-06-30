# Disciplina: Programação Orientada a Objetos
# Semestre: 2023/1

# Importação de bibliotecas
import os
import platform
import json
from datetime import datetime

# Classe para definição de um profissional
class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome.title()
        self.__especialidade = especialidade.title()
        self.__sala = sala

    # Método para obter o nome do profissional
    def get_nome(self):
        return self.__nome

    # Método para obter a especialidade do profissional
    def get_especialidade(self):
        return self.__especialidade

    # Método para obter a sala do profissional
    def get_sala(self):
        return self.__sala

# Classe para definição de um visitante
class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome.title()
        self.__documento = documento

    # Método para obter o nome do visitante
    def get_nome(self):
        return self.__nome

    # Método para obter o documento do visitante
    def get_documento(self):
        return self.__documento

# Classe para definição de uma visita
class Visita:
    def __init__(self, visitante, profissional):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = datetime.now()

    # Método para obter o visitante
    def get_visitante(self):
        return self.__visitante

    # Método para obter o profissional
    def get_profissional(self):
        return self.__profissional

    # Método para obter a data de entrada do visitante
    def get_data_entrada(self):
        return self.__data_entrada

# Função para limpar a tela
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Listas e dicionários para armazenar os dados de profissionais, visitantes e visitas
l_profissionais = []
l_visitantes = []
dict_visitas = {}

# Função para cadastrar profissional
def cadastrar_profissional():
    nome = input("Informe o nome do profissional: ").title()
    especialidade = input("Informe a especialidade do profissional: ").upper()
    sala = input("Informe a sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")

# Função para cadastrar visitante
def cadastrar_visitante():
    nome = input("Informe o nome do visitante: ").title()
    documento = input("Informe o documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)
    print("Visitante cadastrado com sucesso!")

# Função para localizar profissional
def localizar_profissional():
    nome = input("Informe o nome do profissional: ").title()
    for profissional in l_profissionais:
        if profissional.get_nome() == nome:
            print(f"Nome: {profissional.get_nome()} | Especialidade: {profissional.get_especialidade()} | Sala: {profissional.get_sala()}")
            return
    print("Profissional não encontrado.")

# Função para registrar visita
def registrar_visita():
    nome_visitante = input("Informe o nome do visitante: ").title()
    visitante = next((v

 for v in l_visitantes if v.get_nome() == nome_visitante), None)
    
    if visitante is None:
        print("Visitante não encontrado. Deseja cadastra-lo? (S/N)")
        opcao = input().upper()
        if opcao == "S":
            cadastrar_visitante()
            return
        else:
            return

    nome_profissional = input("Informe o nome do profissional: ").title()
    profissional = next((p for p in l_profissionais if p.get_nome() == nome_profissional), None)
    
    if profissional is None:
        print("Profissional não encontrado. Deseja cadastra-lo? (S/N)")
        opcao = input().upper()
        if opcao == "S":
            cadastrar_profissional()
            return
        else:
            return

    visita = Visita(visitante, profissional)
    dict_visitas[visitante.get_nome()] = {
        "nome_profissional": profissional.get_nome(),
        "hora_entrada": visita.get_data_entrada().strftime('%Y-%m-%d %H:%M:%S'),
        "sala": profissional.get_sala()
    }

# Função para gerar relatório de conferência
def relatorio_conferencia():
    clear()
    print("""
    ======================
    MENU RELATÓRIO
    ======================
    1- Consultar por profissional
    2- Consultar por visitante
    3- Consultar por data
    Escolha:""")
    escolha = input()

    if escolha == '1':
        nome_profissional = input("Informe o nome do profissional: ")
        for visitante, info in dict_visitas.items():
            if info['nome_profissional'] == nome_profissional:
                print(f"Visitante: {visitante} | Data da visita: {info['hora_entrada']}")

    elif escolha == '2':
        nome_visitante = input("Informe o nome do visitante: ")
        if nome_visitante in dict_visitas:
            info = dict_visitas[nome_visitante]
            print(f"Profissional: {info['nome_profissional']} | Data da visita: {info['hora_entrada']} | Sala: {info['sala']}")

    elif escolha == '3':
        data_consulta = input("Informe a data (formato: YYYY-MM-DD): ")
        for visitante, info in dict_visitas.items():
            data_visita = info['hora_entrada'].split()[0]
            if data_visita == data_consulta:
                print(f"Visitante: {visitante} | Profissional: {info['nome_profissional']} | Sala: {info['sala']}")

# Função para gerar arquivo de registros
def gerar_arquivo_registros():
    data = {}
    for visitante in l_visitantes:
        if visitante.get_nome() in dict_visitas:
            data[visitante.get_documento()] = dict_visitas[visitante.get_nome()]
    with open('registros.json', 'w') as file:
        json.dump(data, file)

# Função para ler arquivos de profissionais e visitantes
def ler_arquivos():
    try:
        with open('profissionais.txt', 'r') as file:
            for line in file:
                nome, especialidade, sala = line.strip().split(':')
                profissional = Profissional(nome, especialidade, sala)
                l_profissionais.append(profissional)

        with open('visitantes.txt', 'r') as file:
            for line in file:
                nome, documento = line.strip().split(':')
                visitante = Visitante(nome, documento)
                l_visitantes.append(visitante)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

# Função principal
def menu():
    while True:
        clear()
        ler_arquivos()
        print("""
        ======================
        MENU
        ======================
        1- Cadastrar Profissional
        2- Cadastrar Visitante
        3- Localizar Profissional
        4- Registrar Visita
        5- Relatório de Conferência
        6- Gerar arquivo de Registros do dia
        7- Ler arquivos profissionais / visitantes
        8- Sair
        Escolha:""")
        escolha = input()

        if escolha == '1':
            cadastrar_profissional()
        elif escolha == '2':
            cadastrar_visitante()
        elif escolha == '3':
            localizar_profissional()
        elif escolha == '4':
            registrar_visita()
        elif escolha == '5':
            relatorio_conferencia()
        elif escolha == '6':
            gerar_arquivo_registros()
        elif escolha == '7':
            ler_arquivos()
        elif escolha == '8':
            break

# Executa a função principal
if __name__ == "__main__":
    menu()
