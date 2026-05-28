import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

class Cachorro:
    def __init__(self, nome, cor, acordado=True):  #Metodo construtor (inicializador) com os atributos. É importante usar o SELF
        print("Inicializando a Classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    
    def __del__ (self):
       # pass  -> A palavra-chave pass é uma ferramenta útil no Python que ajuda a manter a estrutura do código enquanto você está trabalhando em sua lógica
        print("Destruindo a instância")


    # def __str__(self):
    #     return f"Cachorro(Nome: {self.nome}, Cor: {self.cor}, Status de acordado: {self.acordado})"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

             




P1 = Cachorro("Amora", "Preta", True)
print(P1)


