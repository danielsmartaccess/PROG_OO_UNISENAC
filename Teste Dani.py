class Porta:
    
    # Construtor da classe Porta, que recebe como parâmetros:
    # material (obrigatório), altura (default = 210), largura (default = 80),
    # cor (default = None), aberta (default = None) e instalada (default = None).
    def __init__(self, material, altura=210, largura=80, cor=None, aberta=None, instalada=None):
        # Definição dos atributos da classe Porta, com o uso do prefixo "__" para torná-los privados.
        self.__altura = altura
        self.__largura = largura
        self.__material = material
        self.__cor = cor
        self.__aberta = aberta
        self.__instalada = instalada
        
    # Método getter para o atributo "altura".
    def get_altura(self):
        return self.__altura
    
    # Método getter para o atributo "largura".
    def get_largura(self):
        return self.__largura
    
    # Método getter para o atributo "material".
    def get_material(self):
        return self.__material
    
    # Método getter para o atributo "cor".
    def get_cor(self):
        return self.__cor
    
    # Método setter para o atributo "cor".
    def set_cor(self, cor):
        self.__cor = cor
    
    # Método que verifica se a porta está aberta.
    def is_aberta(self):
        return self.__aberta
    
    # Método que abre a porta, somente se ela estiver instalada.
    def abrir(self):
        if self.is_instalada():
            self.__aberta = True
        else:
            print("A porta não está instalada.")
    
    # Método que fecha a porta, somente se ela estiver instalada.
    def fechar(self):
        if self.is_instalada():
            self.__aberta = False
        else:
            print("A porta não está instalada.")
    
    # Método que verifica se a porta está instalada.
    def is_instalada(self):
        return self.__instalada
    
    # Método que instala a porta.
    def instalar(self):
        self.__instalada = True
    
    # Método que desinstala a porta.
    def desinstalar(self):
        self.__instalada = False
    
    # Método que pinta a porta com a cor informada, somente se ela estiver instalada.
    def pintar(self, cor):
        if self.is_instalada():
            self.__cor = cor
        else:
            print("A porta não está instalada.")
#Criar um método para visualizar os dados. Obs.: Caso a porta não esteja  instalada, imprimir a mensagem: “Pota não instalada.”
    def visualizar(self):
        if self.is_instalada():
            print("Altura: ", self.__altura)
            print("Largura: ", self.__largura)
            print("Material: ", self.__material)
            print("Cor: ", self.__cor)
            print("Aberta: ", self.__aberta)
            print("Instalada: ", self.__instalada)
        else:
            print("Porta não instalada.")
            
#crie outro método vizualisar, que imprima os dados da porta usando __str__  usando format ou f-string
    def __str__(self):
        if self.is_instalada():
            return f"""
            Altura: {self.__altura} 
            Largura: {self.__largura} 
            Material: {self.__material}
            Cor: {self.__cor}
            Aberta: {self.__aberta}
            Instalada: {self.__instalada}
            """
        
#Declare uma lista de larguras de portas aceitaveis. list_largura_postas = [60, 70, 80, 90, 100]


#Crie uma função - escolher_largura_porta - que receba a lista de larguras de portas como parâmetro e retorne uma das opções da lista.

# Altere o construtor da classe Porta para receber a largura como parâmetro e atribuir o valor à largura da porta.

porta1 = Porta("Madeira")
porta1.visualizar()
porta1.instalar()
porta1.visualizar()
porta2 = Porta("PVC", 210, 80, "Vermelho", False, True)
print (porta2)
print (porta1)
porta3 = Porta ("Alumínio", 500, 80, "Azul", True, True)
porta3.set_cor("Amarelo")
print (porta3)