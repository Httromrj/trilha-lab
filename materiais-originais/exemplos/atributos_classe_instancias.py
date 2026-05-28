import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores (*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Rômulo", 1001001)
aluno_2 = Estudante("Max", 1001002)   
mostrar_valores(aluno_1,aluno_2)

print("")
Estudante.escola = "Vida"
aluno_3 = Estudante("Cristiano", 1001003)
mostrar_valores(aluno_1, aluno_2,aluno_3)
