import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
#print(df.head())
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())

'''
# Removendo as linhas com valores ausentes
dt_limpo = df.dropna()
print(dt_limpo.head())



# Preenchendo os valores ausentes com a média da coluna
df['Age'] = df['Age'].fillna(df['Age'].mean())  # FILLNA - Preenche os valores ausentes com a média da coluna 'Age'
print(df['Age'].isnull().sum())
print(df.head())



# Normalização e padronização - Transformação dos dados para uma escala comum
df['Age_log'] = df["Age"].apply(lambda x: x)
print(df['Age_log'])


# Normalização - Escala os valores para um intervalo específico (geralmente entre 0 e 1)
df["Fare_normalized"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())
print(df.head())


'''

#Pipelines - Encadeamento de etapas de pré-processamento
    #1- Importando as bibliotecas necessárias
    #2- limpeza dos dados
    #3- normalização dos dados      
    #4- Gerar dataset final para análise ou modelagem

def limpar_dados(df):
    df = df.copy()  # Criar uma cópia do DataFrame para evitar modificar o original

    df["Age"] =df['Age'].fillna(
        df['Age'].mean()
        )  # Preencher os valores ausentes com a média da coluna 'Age'
    df['Fare_normalized'] = (
        (df['Fare'] - df['Fare'].min()) 
        / (df['Fare'].max() - df['Fare'].min())
           )  # Normalização da coluna 'Fare'
    
    df["Cabin"] = df["Cabin"].fillna("Unknown") # Preencher os valores ausentes na coluna 'Cabin' com a string "Unknown"
    #df["Tem_Cabine"] = df["Cabin"].notna()  # Criar uma nova coluna 'Tem_Cabine' indicando se a cabine está presente ou ausente
    return df

df = limpar_dados(df)
print(df.head())



def validar_dataset(df):
    print("Linhas: ", df.shape[0])
    print("Colunas: ", df.shape[1])
    print("\nValores ausentes por coluna:")
    print(df.isnull().sum())

validar_dataset(df)

'''
    assert df["Age"].isnull().sum() == 0, "Existem valores ausentes na coluna 'Age'"
    assert df["Fare_normalized"].isnull().sum() == 0, "Existem valores ausentes na coluna 'Fare_normalized'"
    assert df["Cabin"].isnull().sum() == 0, "Existem valores ausentes na coluna 'Cabin'"
    print("Validação concluída: O dataset está limpo e normalizado.\n")
'''  
