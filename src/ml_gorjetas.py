"""Primeiro modelo de regressão usando a base de gorjetas."""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parents[1]
ARQUIVO = BASE_DIR / "dados" / "relatorio_gorjetas.csv"


def main():
    df = pd.read_csv(ARQUIVO)

    x = df[["total_bill"]]
    y = df["tip"]

    x_treino, x_teste, y_treino, y_teste = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    modelo = LinearRegression()
    modelo.fit(x_treino, y_treino)

    previsoes = modelo.predict(x_teste)

    print("Modelo: regressão linear")
    print(f"MAE: {mean_absolute_error(y_teste, previsoes):.2f}")
    print(f"R2: {r2_score(y_teste, previsoes):.2f}")

    conta = pd.DataFrame({"total_bill": [100.0]})
    gorjeta_prevista = modelo.predict(conta)[0]
    print(f"Previsão de gorjeta para conta de 100.00: {gorjeta_prevista:.2f}")


if __name__ == "__main__":
    main()

