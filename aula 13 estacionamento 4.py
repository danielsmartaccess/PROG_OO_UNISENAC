# Primeiro, importamos a biblioteca datetime para lidar com datas e horários.
import datetime

# Definimos uma classe Veiculo que vai representar cada veículo que entra no estacionamento.
class Veiculo:
    # O construtor da classe recebe a placa e o horário de entrada. O horário de saída é opcional.
    def __init__(self, placa, entrada, saida=None):
        self.placa = placa
        self.entrada = entrada
        self.saida = saida

# Definimos uma classe Estacionamento que vai representar o estacionamento.
class Estacionamento:
    # O construtor da classe recebe o nome do estacionamento e o número de vagas.
    def __init__(self, nome, vagas):
        self.nome = nome
        # As vagas são representadas por um dicionário onde as chaves são os números das vagas e os valores são os veículos.
        self.vagas = {i+1: None for i in range(vagas)}

    # Método para registrar a entrada de um veículo.
    def entrada_veiculo(self):
        # Buscamos a primeira vaga disponível.
        vaga_disponivel = next((vaga for vaga, veiculo in self.vagas.items() if veiculo is None), None)
        if vaga_disponivel:
            # Solicitamos a placa do veículo.
            placa = input("Informe a placa do veículo: ")
            # Solicitamos o horário de entrada.
            horario_entrada = input("Informe a data e o horário de entrada (formato: DD-MM-AAAA HH:MM) ou deixe em branco para assumir a data e hora atual: ")
            # Se o usuário não informar o horário de entrada, assumimos a data e hora atual.
            horario_entrada = datetime.datetime.strptime(horario_entrada, "%d-%m-%Y %H:%M") if horario_entrada else datetime.datetime.now()
            # Criamos um novo veículo e associamos ele à vaga disponível.
            veiculo = Veiculo(placa, horario_entrada)
            self.vagas[vaga_disponivel] = veiculo
            print(f"Veículo de placa {placa} entrou em {horario_entrada} na vaga {vaga_disponivel}")
        else:
            # Se não houver vagas disponíveis, informamos ao usuário.
            print("Estacionamento lotado.")

    # Método para registrar a saída de um veículo.
    def saida_veiculo(self):
        # Solicitamos a placa do veículo.
        placa = input("Informe a placa do veículo: ")
        # Buscamos o veículo com a placa informada.
        for vaga, veiculo in self.vagas.items():
            if veiculo and veiculo.placa == placa:
                # Solicitamos o horário de saída.
                horario_saida = input("Informe a data e o horário de saída (formato: DD-MM-AAAA HH:MM) ou deixe em branco para assumir a data e hora atual: ")
                # Se o usuário não informar o horário de saída, assumimos a data e hora atual.
                horario_saida = datetime.datetime.strptime(horario_saida, "%d-%m-%Y %H:%M") if horario_saida else datetime.datetime.now()
                veiculo.saida = horario_saida
                # Calculamos a duração da estadia do veículo em horas.
                duracao = (horario_saida - veiculo.entrada).total_seconds()//3600
                # Calculamos o valor a ser pago com base na duração da estadia. A taxa é de R$5,00 por hora.
                valor = duracao * 5
                print(f"Veículo de placa {placa} entrou em {veiculo.entrada} e saiu em {horario_saida} da vaga {vaga}. Valor a ser pago: R$ {valor:.2f}")
                # Liberamos a vaga.
                self.vagas[vaga] = None
                break
        else:
            # Se não encontrarmos o veículo, informamos ao usuário.
            print("Veículo não encontrado")

    # Método para exibir o resumo de ocupação do estacionamento.
    def resumo_ocupacao(self):
        print(f"Total de vagas: {len(self.vagas)}")
        # Percorremos todas as vagas e exibimos o número da vaga e o status dela (Ocupada ou Livre).
        for vaga, veiculo in self.vagas.items():
            status = 'Ocupada' if veiculo else 'Livre'
            print(f"Vaga {vaga}: {status}")

# Função para exibir o menu ao usuário e tratar as opções escolhidas.
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

# Solicitamos ao usuário o nome do estacionamento e o número de vagas.
nome_estacionamento = input("Digite o nome do estacionamento: ")
num_vagas = int(input("Digite o número de vagas do estacionamento: "))
# Criamos o estacionamento.
estacionamento = Estacionamento(nome_estacionamento, num_vagas)
# Exibimos o menu ao usuário.
menu(estacionamento)
