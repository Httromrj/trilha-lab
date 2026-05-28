import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pyodbc  # pip install pyodbc pandas
import pandas as pd

# conexão
conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SERVIDOR;"
    "DATABASE=MinhaBase;"
    "UID=usuario;"
    "PWD=senha"
)

# consulta
query = """
SELECT TOP 10 *
FROM clientes
"""

# jogar resultado para dataframe
df = pd.read_sql(query, conexao)

print(df)

conexao.close()
