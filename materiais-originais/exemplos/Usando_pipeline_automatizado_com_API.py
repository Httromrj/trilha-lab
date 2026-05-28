import pandas as pd
'''
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
print(df.head())

total_gorjetas = df["tip"].sum()
print(f"\nTotal de gorjetas: {total_gorjetas}")

gorjetas_por_dia = df.groupby("day")["tip"].sum() # Agrupa por dia e soma as gorjetas
print("\nGorjetas por dia:", gorjetas_por_dia)  
'''



def pipeline_restaurante():

    # carregar dados
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
    df = pd.read_csv(url)

    # cálculos
    total_gorjetas = df["tip"].sum()

    gorjetas_por_dia = (
        df.groupby("day")["tip"]
        .sum()
    )

    # montar relatório
    relatorio = f"Total geral: {total_gorjetas:.2f}\n\n"
    relatorio += "Total por dia:\n"

    for dia, valor in gorjetas_por_dia.items():
        relatorio += f"{dia}: {valor:.2f}\n"

    # salvar
    with open(
        "relatorio_gorjetas.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
    print(relatorio)


pipeline_restaurante()
