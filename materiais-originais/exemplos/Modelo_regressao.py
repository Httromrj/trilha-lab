import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/ageron/data/main/housing/housing.csv"

df = pd.read_csv(url)
#print(df.head(10))

df = df.dropna() # Removendo as linhas com valores ausentes
x = df.drop(columns=["median_house_value"]) # Removendo a coluna 'median_house_value' (variável alvo)
x = pd.get_dummies(x)
y= df["median_house_value"]


x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
    )


modelo = LinearRegression()
modelo.fit(x_train, y_train)
y_pred = modelo.predict(x_test)


residuos = y_test - y_pred



plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuos)
plt.axhline(y=0, color='r', linestyle='--') 
plt.xlabel('Valores Preditos')
plt.ylabel('Resíduos')
plt.title('Gráfico de Resíduos Vs Valores Preditos')
plt.show()



#NOTA:   LER SOBRE MÉTRICA DE REGREÇÃO - R², MAE, MSE, RMSE