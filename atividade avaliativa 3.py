import PIL


class Relevancia:
    def __init__(self, desemprego, etica, seguranca, regulamentacao, potencial):
        self.desemprego = desemprego
        self.etica = etica
        self.seguranca = seguranca
        self.regulamentacao = regulamentacao
        self.potencial = potencial

#Função limpa tela e inicia no topo do terminal
def clear():
    print("\033[H\033[J")

# Função para verificar se a entrada está dentro do intervalo de votação
def get_valid_vote(prompt):
    while True:
        # Tratamento de exceção para verificar se o valor inserido é um número
        try:
            vote = int(input(prompt))
            if 1 <= vote <= 5:
                return vote
            else:
                print("Valor inválido. Por favor, insira um número entre 1 e 5.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número entre 1 e 5.")

def get_valid_escolha(prompt):
    while True:
        # Tratamento de exceção para verificar se o valor inserido é um número
        try:
            escolha = int(input(prompt))
            if 0 <= escolha <= 3:
                return escolha
            else:
                print("Valor inválido. Por favor, insira um número entre 0 e 3.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número entre 0 e 3.")

pesquisa = {}

estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 
           'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

# Loop principal do programa
while True:
    print("Menu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    escolha = get_valid_escolha("Escolha: ")

    #Chamar função limpa tela
    clear()

    if escolha == 0:
        break
    elif escolha == 1:
        while True:
            estado = input("Informe o estado (sigla) onde você reside: ").upper()
            if estado not in estados:
                print("Estado inválido. Por favor, informe a sigla correta.").upper()
            else:
                break

        desemprego = get_valid_vote("Avalie o Desemprego e Desigualdade (1-5): ")
        etica = get_valid_vote("Avalie Questões Éticas e Morais (1-5): ")
        seguranca = get_valid_vote("Avalie a Segurança Cibernética e Privacidade (1-5): ")
        regulamentacao = get_valid_vote("Avalie o Controle e Regulamentação (1-5): ")
        potencial = get_valid_vote("Avalie o Potencial de Desenvolvimento de IA Superinteligente (1-5): ")

        relevancia = Relevancia(desemprego, etica, seguranca, regulamentacao, potencial)
        clear()


        if estado in pesquisa:
            pesquisa[estado].append(relevancia)
        else:
            pesquisa[estado] = [relevancia]
    elif escolha == 2:
        while True:
            estado = input("Informe o estado (sigla) para o relatório: ").upper()
            if estado not in estados:
                print("Estado inválido. Por favor, informe a sigla correta.")
            else:
                break
       
        # Verificar se o estado informado está na pesquisa
        if estado in pesquisa:
            # Tive que somar todos os valores de cada tópico e dividir pela quantidade de votos
            total_desemprego = sum([r.desemprego for r in pesquisa[estado]])
            total_etica = sum([r.etica for r in pesquisa[estado]])
            total_seguranca = sum([r.seguranca for r in pesquisa[estado]])
            total_regulamentacao = sum([r.regulamentacao for r in pesquisa[estado]])
            total_potencial = sum([r.potencial for r in pesquisa[estado]])
            
            #corrigir o erro de não imprimir o estado como usar .format?
            print(f"RELATÓRIO DO ESTADO: {estado}")
            print("--------------------------------")
            print("Relatório do {}".format(estado))
            #tive que formatar a saída para 2 casas decimais
            print("Desemprego: {:.2f}".format(total_desemprego / len(pesquisa[estado])))
            print("Ética: {:.2f}".format(total_etica / len(pesquisa[estado])))
            print("Segurança: {:.2f}".format(total_seguranca / len(pesquisa[estado])))
            print("Regulamentação: {:.2f}".format(total_regulamentacao / len(pesquisa[estado])))
            print("IA Superinteligente: {:.2f}".format(total_potencial / len(pesquisa[estado])))
            #colocar uma espera para o usuário ler o relatório
            input("Pressione ENTER para continuar...")
            clear()
        else:
            print("Não há dados para o estado informado.")

