"Criar um código usabdio listas e dicionários para gerenciar um estacionamento. NO MENU QUERO AS OPÇÕES: 1 - Entrada de veículo 2 - Saída de veículo 3 - Listar veículos 4 - Sair   O programa deve ficar em loop até que a opção 4 seja escolhida. 1 - Entrada de veículo: deve pedir a placa do veículo e o horário de entrada. Deve guardar essas informações em um dicionário e adicionar esse dicionário em uma lista. 2 - Saída de veículo: deve pedir a placa do veículo e o horário de saída. Deve procurar na lista o dicionário com a placa informada e calcular o valor a ser pago (R$ 5,00 por hora). Deve imprimir na tela a placa, o horário de entrada, o horário de saída e o valor a ser pago. 3 - Listar veículos: deve imprimir na tela todos os veículos que estão no estacionamento. 4 - Sair: deve sair do programa."
#Menu para o usuário        
# 1 - Entrada de veículo
# 2 - Saída de veículo
# 3 - Listar veículos
# 4 - Sair


# 1 - Entrada de veículo: deve pedir a placa do veículo e o horário de entrada. Deve guardar essas informações em um dicionário e adicionar esse dicionário em uma lista.

# 2 - Saída de veículo: deve pedir a placa do veículo e o horário de saída. Deve procurar na lista o dicionário com a placa informada e calcular o valor a ser pago (R$ 5,00 por hora). Deve imprimir na tela a placa, o horário de entrada, o horário de saída e o valor a ser pago.

# 3 - Listar veículos: deve imprimir na tela todos os veículos que estão no estacionamento.

# 4 - Sair: deve sair do programa.

import datetime

class Estacionamento:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = vagas
        self.veiculos = []

    def entrada_veiculo(self):
        if len(self.veiculos) < self.vagas:
            placa = input("Informe a placa do veículo: ")
            horario_entrada = input("Informe o horário de entrada (formato 24h: HH:MM): ")
            horario_entrada = datetime.datetime.strptime(horario_entrada, "%H:%M")
            veiculo = {'placa': placa, 'entrada': horario_entrada}
            self.veiculos.append(veiculo)
            print(f"Veículo de placa {placa} entrou às {horario_entrada}")
        else:
            print("Estacionamento lotado.")

    def saida_veiculo(self):
        placa = input("Informe a placa do veículo: ")
        for veiculo in self.veiculos:
            if veiculo['placa'] == placa:
                horario_saida = input("Informe o horário de saída (formato 24h: HH:MM): ")
                horario_saida = datetime.datetime.strptime(horario_saida, "%H:%M")
                duracao = (horario_saida - veiculo['entrada']).seconds//3600
                valor = duracao * 5
                print(f"Veículo de placa {placa} entrou às {veiculo['entrada'].time()} e saiu às {horario_saida.time()}. Valor a ser pago: R$ {valor:.2f}")
                self.veiculos.remove(veiculo)
                break
        else:
            print("Veículo não encontrado")

    def listar_veiculos(self):
        if self.veiculos:
            for veiculo in self.veiculos:
                print(f"Placa: {veiculo['placa']}, Entrada: {veiculo['entrada'].time()}")
        else:
            print("Estacionamento vazio")

    def resumo_ocupacao(self):
        print(f"Total de vagas: {self.vagas}")
        print(f"Vagas ocupadas: {len(self.veiculos)}")
        print(f"Vagas livres: {self.vagas - len(self.veiculos)}")

def menu(estacionamento):
    while True:
        print("\n*** Menu ***")
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Listar veículos")
        print("4 - Resumo de ocupação")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            estacionamento.entrada_veiculo()
        elif opcao == 2:
            estacionamento.saida_veiculo()
        elif opcao == 3:
            estacionamento.listar_veiculos()
        elif opcao == 4:
            estacionamento.resumo_ocupacao()
        elif opcao == 5:
            break
        else:
            print("Opção inválida, tente novamente.")

nome_estacionamento = input("Digite o nome do estacionamento: ")
num_vagas = int(input("Digite o número de vagas do estacionamento: "))
estacionamento = Estacionamento(nome_estacionamento, num_vagas)
menu(estacionamento)

