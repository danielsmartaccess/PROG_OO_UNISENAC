class Relevancia:
    def __init__(self, desemprego, etica, seguranca, regulamentacao, potencial):
        self.desemprego = desemprego
        self.etica = etica
        self.seguranca = seguranca
        self.regulamentacao = regulamentacao
        self.potencial = potencial

pesquisa = {}

# Lista com todas as siglas dos estados
estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 
           'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

while True:
    print("Menu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    escolha = int(input("Escolha: "))

    if escolha == 0:
        break
    elif escolha == 1:
        while True:
            estado = input("Informe o estado (sigla) onde você reside: ").upper()
            # Verificando se o estado informado é válido
            if estado not in estados:
                print("Estado inválido. Por favor, informe a sigla correta.")
            else:
                break
        desemprego = int(input("Avalie o Desemprego e Desigualdade (1-5): "))
        etica = int(input("Avalie Questões Éticas e Morais (1-5): "))
        seguranca = int(input("Avalie a Segurança Cibernética e Privacidade (1-5): "))
        regulamentacao = int(input("Avalie o Controle e Regulamentação (1-5): "))
        potencial = int(input("Avalie o Potencial de Desenvolvimento de IA Superinteligente (1-5): "))

        relevancia = Relevancia(desemprego, etica, seguranca, regulamentacao, potencial)

        if estado in pesquisa:
            pesquisa[estado].append(relevancia)
        else:
            pesquisa[estado] = [relevancia]
    elif escolha == 2:
        while True:
            estado = input("Informe o estado (sigla) para o relatório: ").upper()
            # Verificando se o estado informado é válido
            if estado not in estados:
                print("Estado inválido. Por favor, informe a sigla correta.")
            else:
                break

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
