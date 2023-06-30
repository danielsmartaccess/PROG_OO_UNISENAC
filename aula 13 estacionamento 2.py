import datetime

class Estacionamento:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = vagas
        self.veiculos = []

    def entrada_veiculo(self):
        if len(self.veiculos) < self.vagas:
            placa = input("Informe a placa do veículo: ")
            horario_entrada = input("Informe o horário de entrada (formato 24h: HH:MM) ou deixe em branco para assumir a hora atual: ")
            horario_entrada = datetime.datetime.strptime(horario_entrada, "%H:%M") if horario_entrada else datetime.datetime.now()
            veiculo = {'placa': placa, 'entrada': horario_entrada}
            self.veiculos.append(veiculo)
            print(f"Veículo de placa {placa} entrou às {horario_entrada.time()}")
        else:
            print("Estacionamento lotado.")

    def saida_veiculo(self):
        placa = input("Informe a placa do veículo: ")
        for veiculo in self.veiculos:
            if veiculo['placa'] == placa:
                horario_saida = input("Informe o horário de saída (formato 24h: HH:MM) ou deixe em branco para assumir a hora atual: ")
                horario_saida = datetime.datetime.strptime(horario_saida, "%H:%M") if horario_saida else datetime.datetime.now()
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
