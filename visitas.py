# Importação das bibliotecas necessárias.
from datetime import datetime
import json


# Definição da classe Profissional.
class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    # Métodos getters para os atributos da classe.
    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala


# Definição da classe Visitante.
class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    # Métodos getters para os atributos da classe.
    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento


# Definição da classe Visita.
class Visita:
    def __init__(self, visitante, profissional):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = datetime.now()

    # Métodos getters para os atributos da classe.
    def get_visitante(self):
        return self.__visitante

    def get_profissional(self):
        return self.__profissional

    def get_data_entrada(self):
        return self.__data_entrada


# Listas para armazenar os objetos das classes Profissional e Visitante.
l_profissionais = []
l_visitantes = []

# Dicionário para armazenar os objetos da classe Visita.
dict_visitas = {}

# Função principal que apresenta o menu ao usuário e lida com a sua escolha.
def menu():
    while True:
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

# Função para cadastrar profissionais. Cada profissional é armazenado como um objeto na lista l_profissionais.
def cadastrar_profissional():
    nome = input("Informe o nome do profissional: ").title
    especialidade = input("Informe a especialidade do profissional: ").title
    sala = input("Informe a sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)

# Função para cadastrar visitantes. Cada visitante é armazenado como um objeto na lista l_visitantes.
def cadastrar_visitante():
    nome = input("Informe o nome do visitante: ").title()
    documento = input("Informe o documento do visitante: ")
    visitante = Visitante(nome, documento)
    l_visitantes.append(visitante)

# Função para localizar um profissional na lista l_profissionais.
def localizar_profissional():
    nome = input("Informe o nome do profissional: ").title()
    for profissional in l_profissionais:
        if profissional.get_nome() == nome:
            print(f"Nome: {profissional.get_nome()} | Especialidade: {profissional.get_especialidade()} | Sala: {profissional.get_sala()}")
            return
    print("Profissional não encontrado.")

# Função para registrar uma visita. A visita é armazenada como um objeto no dicionário dict_visitas.
def registrar_visita():
    nome_visitante = input("Informe o nome do visitante: ").title()
    visitante = next((v for v in l_visitantes if v.get_nome() == nome_visitante), None)
    if visitante is None:
        print("Visitante não encontrado.")
        return

    nome_profissional = input("Informe o nome do profissional: ").title()
    profissional = next((p for p in l_profissionais if p.get_nome() == nome_profissional), None)
    if profissional is None:
        print("Profissional não encontrado.")
        return

    visita = Visita(visitante, profissional)
    dict_visitas[visitante.get_nome()] = {
        "nome_profissional": profissional.get_nome(),
        "hora_entrada": visita.get_data_entrada().strftime('%Y-%m-%d %H:%M:%S'),
        "sala": profissional.get_sala()
    }

# Função para exibir o relatório de conferência. O usuário pode escolher entre procurar por visitante, por profissional ou por data.
def relatorio_conferencia():
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
        nome_profissional = input("Informe o nome do profissional: ").title()
        for visitante, info in dict_visitas.items():
            if info['nome_profissional'] == nome_profissional:
                print(f"Visitante: {visitante} | Data da visita: {info['hora_entrada']}")

    elif escolha == '2':
        nome_visitante = input("Informe o nome do visitante: ").title()
        if nome_visitante in dict_visitas:
            info = dict_visitas[nome_visitante]
            print(f"Profissional: {info['nome_profissional']} | Data da visita: {info['hora_entrada']} | Sala: {info['sala']}")

    elif escolha == '3':
        data_consulta = input("Informe a data (formato: YYYY-MM-DD): ")
        for visitante, info in dict_visitas.items():
            data_visita = info['hora_entrada'].split()[0]
            if data_visita == data_consulta:
                print(f"Visitante: {visitante} | Profissional: {info['nome_profissional']} | Sala: {info['sala']}")

# Função para gerar um arquivo de registros no formato JSON.
def gerar_arquivo_registros():
    data = {}
    for visitante in l_visitantes:
        if visitante.get_nome() in dict_visitas:
            data[visitante.get_documento()] = dict_visitas[visitante.get_nome()]
    with open('registros.json', 'w') as file:
        json.dump(data, file)

# Função para ler arquivos de texto contendo informações sobre profissionais e visitantes.
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

if __name__ == "__main__":
    menu()
