# 08 - IA e Machine Learning

## Objetivo

Entender o fluxo básico de Machine Learning sem pular etapas importantes.

## Fluxo mental

1. Definir o problema.
2. Entender os dados.
3. Separar entrada `X` e alvo `y`.
4. Treinar o modelo.
5. Avaliar com métricas.
6. Explicar limitações.

## Exemplo de regressão

```python
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]
y = [2, 4, 6, 8]

modelo = LinearRegression()
modelo.fit(X, y)

print(modelo.predict([[5]]))
```

## Conceitos importantes

- Regressão prevê números.
- Classificação prevê categorias.
- Métrica mede se o modelo está indo bem.
- Overfitting acontece quando o modelo decora em vez de aprender padrões.

## Desafio rápido

Crie um modelo simples para prever gorjeta com base no valor total da conta usando `dados/relatorio_gorjetas.csv`.

