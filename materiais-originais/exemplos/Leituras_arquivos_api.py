import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import requests

url = "https://api.agify.io/?name=alexsander"
resposta = requests.get(url)
dados = resposta.json()

print(resposta.status_code)
#print(resposta.text)
print(dados)
print("Nome: ", dados["name"])
print("Número de registros: ", dados["count"])




#Salvando os dados da API em um arquivo

import json
import requests
url = "https://api.agify.io/?name=Maxuel"
resposta = requests.get(url)
dados = resposta.json()

with open("dados_api.json", "w") as arquivo:
    json.dump(dados, arquivo)
