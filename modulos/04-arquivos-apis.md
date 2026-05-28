# 04 - Arquivos e APIs

## Objetivo

Ler e salvar informações fora do código.

## Arquivos comuns

- TXT: texto simples.
- CSV: tabela simples.
- JSON: estrutura com listas e dicionários.

## Exemplo com JSON

```python
import json

usuario = {"nome": "Ana", "nivel": "iniciante"}

with open("usuario.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuario, arquivo, ensure_ascii=False, indent=2)

with open("usuario.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados["nome"])
```

## APIs

Uma API permite que seu programa converse com outro sistema. Em Python, a biblioteca `requests` é uma forma comum de fazer isso.

## Desafio rápido

Crie um script que leia `dados/usuario.json`, valide se existe `nome` e gere uma mensagem personalizada de boas-vindas.

