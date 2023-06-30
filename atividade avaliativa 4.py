
# Classe para representar a relevância dos diferentes tópicos
class Relevancia:
    def __init__(self, desemprego, etica, seguranca, regulamentacao, potencial):
        self.desemprego = desemprego
        self.etica = etica
        self.seguranca = seguranca
        self.regulamentacao = regulamentacao
        self.potencial = potencial

# Função para limpar a tela e iniciar no topo do terminal
def clear():
    print("\033[H\033[J")

# Função para garantir que a entrada esteja no intervalo de votação (1 a 5)
def get_valid_vote(prompt):
    while True:
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
        try:
            escolha = int(input(prompt))
            if 0 <= escolha <= 2:
                return escolha
            else:
                print("Valor inválido. Por favor, insira um número entre 0 e 2.")
        except ValueError:
            print("Valor inválido. Por favor, insira um número entre 0 e 2.")


pesquisa = {}
"""" Dicionário para guardar as pesquisas """

# Dicionário para guardar os estados e seus respectivos nomes
estados = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
}

# Loop principal do programa
while True:
    print("Menu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    escolha = get_valid_escolha("Escolha: ")

    # Chamar função limpa tela
    clear()

    if escolha == 0:
        break
    elif escolha == 1:
        while True:
            estado = input("Informe o estado (sigla) onde você reside: ").upper()
            if estado not in estados:
                print("Estado inválido. Por favor, informe a sigla correta.")
            else:
                break

        desemprego = get_valid_vote("Avalie o Desemprego e Desigualdade (1-5): ")
        etica = get_valid_vote("Avalie Questões Éticas e Morais (1-5): ")
        seguranca = get_valid_vote("Avalie a Segurança Cibernética e Privacidade (1-5): ")
        regulamentacao = get_valid_vote("Avalie o Controle e Regulamentação (1-5): ")
        potencial = get_valid_vote("Avalie o Potencial de Desenvolvimento de IA Superinteligente (1-5): ")

        relevancia = Relevancia(desemprego, etica, seguranca, regulamentacao, potencial)
        clear()

        # Armazenar a avaliação no dicionário de pesquisa
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
            # Calcular a média de cada tópico
            total_desemprego = sum([r.desemprego for r in pesquisa[estado]])
            total_etica = sum([r.etica for r in pesquisa[estado]])
            total_seguranca = sum([r.seguranca for r in pesquisa[estado]])
            total_regulamentacao = sum([r.regulamentacao for r in pesquisa[estado]])
            total_potencial = sum([r.potencial for r in pesquisa[estado]])

            # Imprimir relatório
            print(f"RELATÓRIO DO ESTADO: {estados[estado]}")
            print("--------------------------------")
            print("Desemprego e Desigualdade: {:.2f}".format(total_desemprego / len(pesquisa[estado])))
            print("Ética e Morais: {:.2f}".format(total_etica / len(pesquisa[estado])))
            print("Segurança Cibernética e Privacidade: {:.2f}".format(total_seguranca / len(pesquisa[estado])))
            print("Controle e Regulamentação: {:.2f}".format(total_regulamentacao / len(pesquisa[estado])))
            print("IA Superinteligente: {:.2f}".format(total_potencial / len(pesquisa[estado])))

            # Aguardar o usuário pressionar ENTER para continuar
            input("Pressione ENTER para continuar...")
            clear()
        else:
            print("Não há dados para o estado informado.")
