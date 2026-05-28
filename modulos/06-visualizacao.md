# 06 - Visualização de Dados

## Objetivo

Criar gráficos que ajudem a entender e comunicar padrões.

## Boas perguntas antes do gráfico

- Quero comparar valores?
- Quero ver evolução?
- Quero ver distribuição?
- Quero ver relação entre duas variáveis?

## Exemplo

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/relatorio_gorjetas.csv")

plt.scatter(df["total_bill"], df["tip"])
plt.xlabel("Conta total")
plt.ylabel("Gorjeta")
plt.title("Relação entre conta e gorjeta")
plt.show()
```

## Desafio rápido

Crie três gráficos:

- dispersão entre conta e gorjeta;
- barras com gorjeta média por dia;
- histograma do valor da conta.

Depois escreva uma frase explicando cada gráfico.

