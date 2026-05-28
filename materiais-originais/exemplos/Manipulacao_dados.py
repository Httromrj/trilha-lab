import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 32]

plt.plot(x, y)
plt.show()



import numpy as np
x = np.array([1, 2, 3, 4, 5])
resultado = x * 2
print(resultado)


import pandas as pd
dados = {'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
         'Idade': [25, 30, 35, 40, 45]}
df = pd.DataFrame(dados)
print(df) 
df.to_csv('dados.csv', index=False) 

#Agora, vamos ler o arquivo CSV que acabamos de criar e exibir seu conteúdo:
import pandas as pd
df = pd.read_csv('dados.csv')
print(df)
print("Media das idades:", df["Idade"].mean()) #Calcula a média da coluna "Idade"
print("Quantidade de pessoas:", df["Nome"].count()) #Calcula a quantidade de pessoas
print("")
print("Analise: \n", df["Nome"].describe())




#Novo exemplo de manipulação de dados usando pandas:
import pandas as pd  
import matplotlib.pyplot as plt

dados = {'Produto': ['Notebook', 'Mouse', 'Teclado', 'Teclado', 'Mouse'],  
         'Preço': [3500, 120, 150, 200, 120]
         }  
df = pd.DataFrame(dados)
df.groupby('Produto').mean()
print(df.groupby('Produto').mean())

plt.bar(df['Produto'], df['Preço'])
plt.show()