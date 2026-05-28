import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#pip install pandas numpy matplotlib seaborn scikit-learn openpyxl
# URL Raw de um dataset público de vendas de supermercado (hospedado no GitHub)
url = "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv"

# Importando os dados
df = pd.read_csv(url)

# Mostrando as 5 primeiras linhas e informações gerais do arquivo
#print("--- Primeiras Linhas do Dataset ---")
#print(df.head())


#plt.scatter(df["total_bill"], df['tip'])
#plt.xlabel("Conta total")
#plt.xlabel("Valor da gorjeta")
#plt.title("Relação entre conta e gorjeta")
#plt.show()

#sns.scatterplot(data=df, x="total_bill", y="tip")
#plt.show()

# fig = px.scatter(
#     df,
#     x = 'total_bill',
#     y = 'tip',
#     color = "day",
#     title = "Relaçao entre conta e gorjeta"
# )
# fig.show()



fig, ax = plt.subplots(1,2, figsize=(10,4))
sns.histplot(df["total_bill"], ax = ax[0])
ax[0].set_title("Distribuição da conta")

sns.boxplot(data=df, x='day', y="tip", ax=ax[1])
ax[1].set_title("Gorjetas por dia")
plt.show()


#print("--- Estatísticas Descritivas ---")
