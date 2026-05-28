# 02 - Coleções e Fluxo

## Objetivo

Organizar vários valores e controlar decisões no programa.

## Coleções principais

- `list`: lista mutável e ordenada.
- `tuple`: sequência imutável.
- `set`: coleção sem repetição.
- `dict`: pares de chave e valor.

## Exemplo

```python
transacao = {
    "descricao": "Curso de Python",
    "categoria": "educacao",
    "valor": 97.50,
}

if transacao["valor"] > 100:
    print("Revisar gasto")
else:
    print("Gasto dentro do esperado")
```

## Laços

```python
categorias = ["educacao", "alimentacao", "transporte"]

for categoria in categorias:
    print(f"Analisando categoria: {categoria}")
```

## Desafio rápido

Receba uma lista de gastos e calcule:

- total;
- maior gasto;
- menor gasto;
- categorias únicas;
- gastos acima de um limite definido por você.

