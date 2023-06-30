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
    
    # Método que abre a porta.
    def abrir(self):
        self.__aberta = True
    
    # Método que fecha a porta.
    def fechar(self):
        self.__aberta = False
    
    # Método que verifica se a porta está instalada.
    def is_instalada(self):
        return self.__instalada
    
    # Método que instala a porta.
    def instalar(self):
        self.__instalada = True
    
    # Método que desinstala a porta.
    def desinstalar(self):
        self.__instalada = False
