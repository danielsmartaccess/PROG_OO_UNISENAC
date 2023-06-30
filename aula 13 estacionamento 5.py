# Primeiro, importamos as bibliotecas necessárias.
import datetime
import json
import os

# Definimos a classe Veiculo, que vai representar cada veículo que entra no estacionamento.
class Veiculo:
    # O construtor recebe a placa e a hora de entrada do veículo.
    def __init__(self, placa, entrada, saida=None):
        self.placa = placa
        self.entrada = entrada
        self.saida = saida

    # Representação do objeto em formato de string, para facilitar a exibição.
    def __str__(self):
        return f'\nPlaca: {self.placa}\nEntrada: {self.entrada}\nSaída: {self.saida}\n'

    # Método para converter o objeto em um dicionário, facilitando a serialização.
    def to_dict(self):
        return {
            'placa': self.placa,
            'entrada': self.entrada.strftime("%d-%m-%Y %H:%M"),
            'saida': self.saida.strftime("%d-%m-%Y %H:%M") if self.saida else None
        }

# Definimos a classe Estacionamento.
class Estacionamento:
    # O construtor recebe o número de vagas.
    def __init__(self, vagas):
        # As vagas são representadas por um dicionário onde as chaves são os números das vagas e os valores são listas de veículos.
        self.vagas = {i: [] for i in range(1, vagas+1)}

    # Método para registrar a entrada de um veículo.
    def entrada_veiculo(self):
        # Procuramos a primeira vaga disponível.
        vaga_disponivel = next((vaga for vaga, veiculos in self.vagas.items() if not veiculos), None)
        if vaga_disponivel is not None:
            # Solicitamos a placa do veículo.
            placa = input("Informe a placa do veículo: ")
            # Solicitamos a data e hora de entrada.
            entrada = input("Informe a data e hora de entrada (formato DD-MM-AAAA HH:MM) ou deixe em branco para usar o momento atual: ")
            # Se o usuário não informar a entrada, assumimos o momento atual.
            entrada = datetime.datetime.strptime(entrada, "%d-%m-%Y %H:%M") if entrada else datetime.datetime.now()
            # Criamos um novo veículo e adicionamos na vaga disponível.
            veiculo = Veiculo(placa, entrada)
            self.vagas[vaga_disponivel].append(veiculo)
        else:
            print("Estacionamento lotado.")

    # Método para registrar a saída de um veículo.
    def saida_veiculo(self):
        # Solicitamos a placa do veículo.
        placa = input("Informe a placa do veículo: ")
        # Procuramos o veículo nas vagas.
        for vaga, veiculos in self.vagas.items():
            for veiculo in veiculos:
                if veiculo.placa == placa:
                    # Solicitamos a data e hora de saída.
                    saida = input("Informe a data e hora de saída (formato DD-MM-AAAA HH:MM) ou deixe em branco para usar o momento atual: ")
                    # Se o usuário não informar a saída, assumimos o momento atual.
                    saida = datetime.datetime.strptime(saida, "%d-%m-%Y %H:%M") if saida else datetime.datetime.now()
                    # Atualizamos a saída do veículo.
                    veiculo.saida = saida
                    # Imprimimos a vaga.
                    print(f"Veículo de placa {placa} saiu da vaga {vaga}")
                    return
        print("Veículo não encontrado")

    # Método para imprimir o resumo de ocupação do estacionamento.
    def resumo_ocupacao(self):
        for vaga, veiculos in self.vagas.items():
            print(f'Vaga {vaga}:')
            for veiculo in veiculos:
                print(f'   {veiculo}')

    # Método para serializar o objeto em um dicionário, facilitando a escrita no arquivo.
    def to_dict(self):
        return {vaga: [veiculo.to_dict() for veiculo in veiculos] for vaga, veiculos in self.vagas.items()}

    # Método para criar um novo objeto a partir de um dicionário, facilitando a leitura do arquivo.
    @staticmethod
    def from_dict(data):
        estacionamento = Estacionamento(len(data))
        estacionamento.vagas = {vaga: [Veiculo(**veiculo) for veiculo in veiculos] for vaga, veiculos in data.items()}
        return estacionamento

# Função para exibir o menu ao usuário e tratar as opções escolhidas.
def menu(estacionamento):
    while True:
        print("\n*** Menu ***")
        print("1 - Entrada de veículo")
        print("2 - Saída de veículo")
        print("3 - Resumo de ocupação")
        print("4 - Salvar e sair")
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

    # Perguntamos ao usuário se ele quer salvar os dados em um arquivo.
    salvar = input("Deseja salvar os dados em um arquivo? (S/N) ").upper()
    if salvar == 'S':
        # Perguntamos ao usuário o tipo de arquivo.
        tipo_arquivo = input("Qual tipo de arquivo deseja utilizar para salvar os dados? (TXT/JSON) ").upper()
        # Criamos o nome do arquivo com base no tipo escolhido.
        nome_arquivo = f'estacionamento.{tipo_arquivo.lower()}'
        # Serializamos o objeto estacionamento.
        data = estacionamento.to_dict()
        # Salvamos os dados no arquivo.
        with open(nome_arquivo, 'w') as f:
            if tipo_arquivo == 'TXT':
                f.write(str(data))
            elif tipo_arquivo == 'JSON':
                json.dump(data, f)
            else:
                print("Tipo de arquivo inválido")

# Verificamos se o arquivo TXT ou JSON já existe.
if os.path.exists('estacionamento.txt'):
    nome_arquivo = 'estacionamento.txt'
elif os.path.exists('estacionamento.json'):
    nome_arquivo = 'estacionamento.json'
else:
    nome_arquivo = None

# Se o arquivo já existir, perguntamos ao usuário se ele quer utilizá-lo.
if nome_arquivo:
    utilizar = input(f"O arquivo {nome_arquivo} já existe. Deseja utilizá-lo? (S/N) ").upper()
    if utilizar == 'S':
        with open(nome_arquivo, 'r') as f:
            if nome_arquivo.endswith('.txt'):
                data = eval(f.read())
            elif nome_arquivo.endswith('.json'):
                data = json.load(f)
        estacionamento = Estacionamento.from_dict(data)
    else:
        vagas = int(input("Informe o número de vagas do estacionamento: "))
        estacionamento = Estacionamento(vagas)
else:
    vagas = int(input("Informe o número de vagas do estacionamento: "))
    estacionamento = Estacionamento(vagas)

# Exibimos o menu ao usuário.
menu(estacionamento)
