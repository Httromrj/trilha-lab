# 07 - Banco de Dados

## Objetivo

Guardar dados de forma estruturada e consultar com SQL.

## Conceitos

- Banco: local onde dados são armazenados.
- Tabela: estrutura com linhas e colunas.
- SQL: linguagem para criar, inserir, consultar e atualizar dados.
- SQLite: banco leve, ótimo para aprender.

## Exemplo

```python
import sqlite3

conexao = sqlite3.connect("dados/jornada.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    pontos INTEGER NOT NULL
)
""")

cursor.execute("INSERT INTO alunos (nome, pontos) VALUES (?, ?)", ("Ana", 10))
conexao.commit()

for linha in cursor.execute("SELECT nome, pontos FROM alunos"):
    print(linha)

conexao.close()
```

## Desafio rápido

Crie uma tabela `missoes` com:

- título;
- módulo;
- status;
- pontuação.

Depois insira três missões e consulte apenas as concluídas.

