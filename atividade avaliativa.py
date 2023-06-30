# Definindo a classe Relevancia para armazenar as avaliações
class Relevancia:
    def __init__(self, desemprego, etica, seguranca, regulamentacao, potencial):
        self.desemprego = desemprego
        self.etica = etica
        self.seguranca = seguranca
        self.regulamentacao = regulamentacao
        self.potencial = potencial

# Criando o dicionário para armazenar as respostas por estado
pesquisa = {}

while True:
    # Mostrando o menu para o usuário
    print("Menu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    escolha = int(input("Escolha: "))

    # Se o usuário escolher finalizar o programa, o loop termina
    if escolha == 0:
        break
    # Se o usuário escolher realizar uma avaliação
    elif escolha == 1:
        # Coletando as informações do usuário
        estado = input("Informe o estado (sigla) onde você reside: ")
        desemprego = int(input("Avalie o Desemprego e Desigualdade (1-5): "))
        etica = int(input("Avalie Questões Éticas e Morais (1-5): "))
        seguranca = int(input("Avalie a Segurança Cibernética e Privacidade (1-5): "))
        regulamentacao = int(input("Avalie o Controle e Regulamentação (1-5): "))
        potencial = int(input("Avalie o Potencial de Desenvolvimento de IA Superinteligente (1-5): "))

        # Criando uma instância da classe Relevancia com as avaliações do usuário
        relevancia = Relevancia(desemprego, etica, seguranca, regulamentacao, potencial)

        # Adicionando a avaliação ao estado correspondente no dicionário
        if estado in pesquisa:
            pesquisa[estado].append(relevancia)
        else:
            pesquisa[estado] = [relevancia]
    # Se o usuário escolher gerar um relatório
    elif escolha == 2:
        # Coletando o estado para o relatório
        estado = input("Informe o estado (sigla) para o relatório: ")

        # Calculando a média de cada tópico para o estado informado
        if estado in pesquisa:
            total_desemprego = sum([r.desemprego for r in pesquisa[estado]])
            total_etica = sum([r.etica for r in pesquisa[estado]])
            total_seguranca = sum([r.seguranca for r in pesquisa[estado]])
            total_regulamentacao = sum([r.regulamentacao for r in pesquisa[estado]])
            total_potencial = sum([r.potencial for r in pesquisa[estado]])

            print("Percentual de importância para cada tópico:")
            print("Desemprego e Desigualdade: ", total_desemprego / len(pesquisa[estado]))
            print("Questões Éticas e Morais: ", total_etica / len(pesquisa[estado]))
            print("Segurança Cibernética e Privacidade: ", total_seguranca / len(pesquisa[estado]))
            print("Controle e Regulamentação: ", total_regulamentacao / len(pesquisa[estado]))
            print("Potencial de Desenvolvimento de IA Superinteligente: ", total_potencial / len(pesquisa[estado]))
        else:
            print("Não há dados para o estado informado.")
