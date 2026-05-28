import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import json

dados = {
    "nome"  : "Angela",
    "idade" : 25,
    "cidade": "Rio de Janeiro"
}

with open ("usuario.json", "w") as arquivos:
    json.dump(dados, arquivos)



#Leitura do JSON

with open ("usuario.json", "r") as arquivos:
    dados = json.load(arquivos)

print(dados)    
