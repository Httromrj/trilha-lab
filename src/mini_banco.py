"""Mini laboratório de SQLite para registrar missões."""

import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / "dados" / "jornada.db"


MISSOES = [
    ("Rodar o quiz inicial", "00", "concluida", 10),
    ("Criar calculadora de metas", "01", "pendente", 20),
    ("Explorar CSV com pandas", "05", "pendente", 30),
]


def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabela(conexao):
    conexao.execute(
        """
        CREATE TABLE IF NOT EXISTS missoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            modulo TEXT NOT NULL,
            status TEXT NOT NULL,
            pontos INTEGER NOT NULL
        )
        """
    )


def popular(conexao):
    total = conexao.execute("SELECT COUNT(*) FROM missoes").fetchone()[0]
    if total == 0:
        conexao.executemany(
            "INSERT INTO missoes (titulo, modulo, status, pontos) VALUES (?, ?, ?, ?)",
            MISSOES,
        )
        conexao.commit()


def listar(conexao):
    consulta = """
        SELECT modulo, titulo, status, pontos
        FROM missoes
        ORDER BY modulo, id
    """
    for modulo, titulo, status, pontos in conexao.execute(consulta):
        print(f"Módulo {modulo} | {status:9} | {pontos:2} pts | {titulo}")


def main():
    with conectar() as conexao:
        criar_tabela(conexao)
        popular(conexao)
        listar(conexao)


if __name__ == "__main__":
    main()

