import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def calcular_dt_nascimento (cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = pessoa.calcular_dt_nascimento(1988, 6, 21, "Rômulo")
print(p.nome, p.idade)

print("")

print("18 Anos, é maior de idade?", pessoa.maior_idade(18))
print( "8 Anos, é maior de idade?", pessoa.maior_idade(8))
