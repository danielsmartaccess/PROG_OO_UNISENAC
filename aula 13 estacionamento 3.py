import datetime

class Veiculo:
    def __init__(self, placa, entrada, saida=None):
        self.placa = placa
        self.entrada = entrada
        self.saida = saida

class Estacionamento:
    def __init__(self, nome, vagas):
        self.nome = nome
        self.vagas = {i+1: None for i in range(vagas)}

    def entrada_veiculo(self):
        vaga_disponivel = next((vaga for vaga, veiculo in self.vagas.items() if veiculo is None), None)
        if vaga_disponivel:
            placa = input("Informe a placa do veículo: ")
            horario_entrada = input("Informe a data e o horário de entrada (formato: DD-MM-AAAA HH:MM) ou deixe em branco para assumir a data e hora atual: ")
            horario_entrada = datetime.datetime.strptime(horario_entrada, "%d-%m-%Y %H:%M") if horario_entrada else datetime.datetime.now()
            veiculo = Veiculo(placa, horario_entrada)
            self.vagas[vaga_disponivel] = veiculo
            print(f"Veículo de placa {placa} entrou em {horario_entrada} na vaga {vaga_disponivel}")
        else:
            print("Estacionamento lotado.")

    def saida_veiculo(self):
        placa = input("Informe a placa do veículo: ")
        for vaga, veiculo in self.vagas.items():
            if veiculo and veiculo.placa == placa:
                horario_saida = input("Informe a data e o horário de saída (formato: DD-MM-AAAA HH:MM) ou deixe em branco para assumir a data e hora atual: ")
                horario_saida = datetime.datetime.strptime(horario_saida, "%d-%m-%Y %H:%M") if horario_saida else datetime.datetime.now()
                veiculo.saida = horario_saida
                duracao = (horario_saida - veiculo.entrada).total_seconds()//3600
                valor = duracao * 5
                print(f"Veículo de placa {placa} entrou em {veiculo.entrada} e saiu em {horario_saida} da vaga {vaga}. Valor a ser pago: R$ {valor:.2f}")
                self.vagas[vaga] = None
                break
        else:
            print("Veículo não encontrado")

    def resumo_ocupacao(self):
        vagas_ocupadas = sum(1 for veiculo in self.vagas.values() if veiculo is not None)
        print(f"Total de vagas: {len(self.vagas)}")
        print(f"Vagas ocupadas: {vagas_ocupadas}")
        print(f"Vagas livres: {len(self.vagas) - vagas_ocupadas}")

def menu(estacionamento):
    while True:
        print("\n*** Menu ***")
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Resumo de ocupação")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            estacionamento.entrada_veiculo()
        elif opcao == 2:
            estacionamento.saida_veiculo()
        elif opcao == 3:
            estacionamento.resumo_ocupacao()
        elif opcao == 4:
            break
        else:
            print("Opção inválida, tente novamente.")

nome_estacionamento = input("Digite o nome do estacionamento: ")
num_vagas = int(input("Digite o número de vagas do estacionamento: "))
estacionamento = Estacionamento(nome_estacionamento, num_vagas)
menu(estacionamento)
