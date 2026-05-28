import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sqlite3
#criando ou conectando ao banco

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    nome TEXT,
    idade INTEGER
               )
               """)

conexao.commit()
conexao.close()


#INSERINDO VALORES NESSA TABELA CRIADA, CHAMADA DADOS.DB

import sqlite3
#criando ou conectando ao banco

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()

cursor.execute(
    "INSERT INTO usuarios VALUES (?, ?)",
        ("Maria", 25)
)
conexao.commit()
conexao.close()




#CONSULTAR VALORES NESSA TABELA CRIADA, CHAMADA DADOS.DB

conexao = sqlite3.connect("dados.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()
print(dados)
