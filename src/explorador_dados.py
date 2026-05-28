"""Resumo rápido de um CSV usando pandas."""

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO = BASE_DIR / "dados" / "relatorio_gorjetas.csv"


def main():
    df = pd.read_csv(ARQUIVO)

    print("Resumo do arquivo")
    print(f"Arquivo: {ARQUIVO.name}")
    print(f"Linhas: {df.shape[0]}")
    print(f"Colunas: {df.shape[1]}")
    print("\nColunas:")
    print(", ".join(df.columns))

    print("\nValores ausentes por coluna:")
    print(df.isna().sum())

    print("\nEstatísticas numéricas:")
    print(df.describe())

    if {"day", "tip"}.issubset(df.columns):
        print("\nGorjeta média por dia:")
        print(df.groupby("day")["tip"].mean().sort_values(ascending=False))


if __name__ == "__main__":
    main()

