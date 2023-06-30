import os
import platform
import json
from datetime import datetime

# Classe que define um profissional
class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome.upper()
        self.__especialidade = especialidade.upper()
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala

# Classe que define um visitante
class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome.upper()
        self.__documento = documento

    def get_nome(self):
        return self.__nome

    def get_documento(self):
        return self.__documento

# Classe que define uma visita
class Visita:
    def __init__(self, visitante, profissional):
        self.__visitante = visitante
        self.__profissional = profissional
        self.__data_entrada = datetime.now()

    def get_visitante(self):
        return self.__visitante

    def get_profissional(self):
        return self.__profissional

    def get_data_entrada(self):
        return self.__data_entrada

# Função para limpar a tela
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

l_profissionais = []
l_visitantes = []
dict_visitas = {}

# Função para cadastrar um profissional
def cadastrar_profissional():
    nome = input("Informe o nome do profissional: ").upper()
    especialidade = input("Informe a especialidade do profissional: ").upper()
    sala = input("Informe a sala do profissional: ")
    profissional = Profissional(nome, especialidade, sala)
    l_profissionais.append(profissional)

# Função para cadastrar um visitante
def cadastrar_visitante(nome_visitante):
    documento = input("Informe o documento do visitante: ")
    visitante = Visitante(nome_visitante, documento)
    l_visitantes.append(visitante)
    print (f"Visitante: {nome_visitante} cadastrado")
    input("Pressione ENTER para continuar...")
 
# Função para localizar um profissional e imprimir seus dados
def localizar_profissional():
    for profissional in l_profissionais:
        nome = profissional.get_nome().ljust(30)
        especialidade = profissional.get_especialidade().ljust(20)
        sala = profissional.get_sala().ljust(20)
        print(f"{nome} | {especialidade} | {sala}")
    input("Pressione ENTER para continuar...")
    return

# Função para registrar uma visita
def registrar_visita():
    nome_visitante = input("Informe o nome do visitante: ").upper()
    visitante = next((v for v in l_visitantes if v.get_nome() == nome_visitante), None)

    if visitante is None:
        print("Visitante não encontrado. Deseja cadastra-lo? (S/N)")
        opcao = input().upper()
        if opcao == "S":
            cadastrar_visitante(nome_visitante)
            return
        else:
            return
        
    while True:
        nome_profissional = input("Informe o nome do profissional: ").upper()
        profissional = next((p for p in l_profissionais if p.get_nome() == nome_profissional), None)
        if profissional is None:
            print("Profissional não encontrado. Digite novamente.")
            localizar_profissional()
            input("Pressione ENTER para continuar...")
        else:
            break
        

    visita = Visita(visitante, profissional)
    dict_visitas[visitante.get_nome()] = {
        "nome_profissional": profissional.get_nome(),
        "hora_entrada": visita.get_data_entrada().strftime('%Y-%m-%d %H:%M:%S'),
        "sala": profissional.get_sala()
    }

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
    clear()
    
    if escolha == '1':
        nome_profissional = input("Informe o nome do profissional: ").upper()
        for nome_profissional, info in dict_visitas.items():
            if info['nome_profissional'] == nome_profissional:
                print(f"Visitante: {visitante} | Data da visita: {info['hora_entrada']}")
        input("Pressione ENTER para continuar...")

    elif escolha == '2':
        nome_visitante = input("Informe o nome do visitante: ").upper()
        if nome_visitante in dict_visitas:
            info = dict_visitas[nome_visitante]
            print(f"Profissional: {info['nome_profissional']} | Data da visita: {info['hora_entrada']} | Sala: {info['sala']}")
        input("Pressione ENTER para continuar...")


    elif escolha == '3':
        data_consulta = input("Informe a data (formato: YYYY-MM-DD): ")          
        for visitante, info in dict_visitas.items():
            data_visita = info['hora_entrada'].split()[0]
            if data_visita == data_consulta:
                print(f"Visitante: {visitante} | Profissional: {info['nome_profissional']} | Sala: {info['sala']}")
        input("Pressione ENTER para continuar...")


def gerar_arquivo_registros():
    data = {}
    for visitante in l_visitantes:
        if visitante.get_nome() in dict_visitas:
            data[visitante.get_documento()] = dict_visitas[visitante.get_nome()]
    with open('registros.json', 'w') as file:
        json.dump(data, file)

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

def menu():
    while True:
        clear()
        ler_arquivos()
        print("""
        ======================
        MENU
        ======================
        1- Registrar Visita
        2- Localizar Profissional
        3- Cadastrar Profissional
        4- Relatório de Conferência
        5- Gerar arquivo de Registros do dia
        6- Sair
        Escolha:""")
        escolha = input()
        clear()

        if escolha == '1':
            registrar_visita()
        elif escolha == '2':
            localizar_profissional()
        elif escolha == '3':
            cadastrar_profissional()
        elif escolha == '4':
            relatorio_conferencia()
        elif escolha == '5':
            gerar_arquivo_registros()
        elif escolha == '6':
            break

if __name__ == "__main__":
    menu()
