import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# URL Raw de um dataset público de vendas de supermercado (hospedado no GitHub)
url = "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv"

# Importando os dados
df = pd.read_csv(url)

# Configura a grade do dashboard (2 linhas, 2 colunas)
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Primeiro gráfico (Superior Esquerdo)
sns.histplot(df["total_bill"], ax=ax[0, 0])
ax[0, 0].set_title("Distribuição das Contas")

# 2. Segundo gráfico (Superior Direito)
sns.boxplot(data=df, x="day", y="tip", ax=ax[0, 1])
ax[0, 1].set_title("Gorjetas por dia")

# 3. Terceiro gráfico (Inferior Esquerdo)
sns.scatterplot(data=df, x="total_bill", y="tip", ax=ax[1, 0])
ax[1, 0].set_title("Conta vs Gorjeta")

# 4. Quarto gráfico (Inferior Direito)
sns.countplot(data=df, x="day", ax=ax[1, 1])
ax[1, 1].set_title("Quantidade de clientes por dia")

# Ajusta o espaçamento e exibe o dashboard
plt.tight_layout()
plt.show()
