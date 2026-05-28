import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

class Veiculo:
    def __init__(self, cor, placa, qtd_rodas):
        self.cor = cor
        self.placa = placa
        self.qtd_rodas = qtd_rodas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, qtd_rodas, carregado):
        super().__init__(cor,placa, qtd_rodas)
        self.carregado = carregado

    def status_carregado (self):
        print(f"{'Sim' if self.carregado else 'Não' } Está com carga!")



moto = Motocicleta("Vermelha", "ABC-123", 2)
carro = Carro ("Cinza Vulca", "KNZ_52526", 4)
carreta = Caminhao ("Branco Perolado", "TBK-2561", 8, True) 

#carreta.status_carregado()
print(moto)
print(carro)
print(carreta)
