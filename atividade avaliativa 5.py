import PIL

class Relevancia:
    def __init__(self, desemprego, etica, seguranca, regulamentacao, potencial):
        self._desemprego = desemprego
        self._etica = etica
        self._seguranca = seguranca
        self._regulamentacao = regulamentacao
        self._potencial = potencial

    @property
    def desemprego(self):
        return self._desemprego

    @desemprego.setter
    def desemprego(self, value):
        self._desemprego = value

    @property
    def etica(self):
        return self._etica

    @etica.setter
    def etica(self, value):
        self._etica = value

    @property
    def seguranca(self):
        return self._seguranca

    @seguranca.setter
    def seguranca(self, value):
        self._seguranca = value

    @property
    def regulamentacao(self):
        return self._regulamentacao

    @regulamentacao.setter
    def regulamentacao(self, value):
        self._regulamentacao = value

    @property
    def potencial(self):
        return self._potencial

    @potencial.setter
    def potencial(self, value):
        self._potencial = value

def clear():
    print("\033[H\033[J")

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

while True:
    print("Menu")
    print("0- Finalizar o Programa")
    print("1- Realizar avaliação")
    print("2- Relatório")
    escolha = get_valid_escolha("Escolha: ")

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

        if estado in pesquisa:
            media_desemprego = sum([r.desemprego for r in pesquisa[estado]]) / len(pesquisa[estado])
            media_etica = sum([r.etica for r in pesquisa[estado]]) / len(pesquisa[estado])
            media_seguranca = sum([r.seguranca for r in pesquisa[estado]]) / len(pesquisa[estado])
            media_regulamentacao = sum([r.regulamentacao for r in pesquisa[estado]]) / len(pesquisa[estado])
            media_potencial = sum([r.potencial for r in pesquisa[estado]]) / len(pesquisa[estado])

            medias = {
                'Desemprego e Desigualdade': media_desemprego,
                'Questões Éticas e Morais': media_etica,
                'Segurança Cibernética e Privacidade': media_seguranca,
                'Controle e Regulamentação': media_regulamentacao,
                'IA Superinteligente': media_potencial
            }

            maior_media = max(medias, key=medias.get)
            print(f"Maior média: {maior_media} com {medias[maior_media]}")

            medias_ordenadas = sorted(medias.items(), key=lambda x: x[1], reverse=True)

            print(f"RELATÓRIO DO ESTADO: {estados[estado]}")
            print("--------------------------------")
            for media in medias_ordenadas:
                print(f"{media[0]}: {media[1]:.2f}")

            input("Pressione ENTER para continuar...")
            clear()
        else:
            print("Não há dados para o estado informado.")
