import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import csv

dados = [
    {"nome","idade", "cidade"},
    {"Camila", 25, "São Paulo"},
    {"Carlos", 30, "Bahia"},
    {"Maria", 28, "Rio de Janeiro"}
]

with open("pessoas.csv", "w", newline="") as arquivo:
    writer = csv.writer (arquivo)
    writer.writerows(dados)



#Lendo um CVS

import csv
with open("pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)
