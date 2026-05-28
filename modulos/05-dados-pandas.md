# 05 - Pandas e Análise de Dados

## Objetivo

Usar DataFrames para explorar, limpar e resumir dados.

## Exemplo

```python
import pandas as pd

df = pd.read_csv("dados/relatorio_gorjetas.csv")

print(df.head())
print(df.info())
print(df.describe())
```

## Perguntas que guiam uma análise

- Quantas linhas e colunas existem?
- Existem valores ausentes?
- Quais colunas são numéricas?
- Quais categorias aparecem mais?
- Existe algum valor muito fora do padrão?

## Desafio rápido

Com o arquivo `dados/relatorio_gorjetas.csv`, descubra:

- média da conta;
- média da gorjeta;
- maior gorjeta;
- dia com maior total de gorjetas;
- percentual médio de gorjeta sobre a conta.

