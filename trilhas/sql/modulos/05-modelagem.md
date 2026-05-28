# 05 - Modelagem de Dados

## Objetivo

Pensar antes de criar tabelas.

## Perguntas de modelagem

- Quais entidades existem?
- Quais atributos cada entidade tem?
- Existe relacionamento entre elas?
- Qual campo identifica cada registro?
- O dado pode se repetir?

## Exemplo

```sql
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cidade TEXT,
    trilha TEXT NOT NULL
);
```

## Missão

Modele um banco para acompanhar estudos com:

- alunos;
- trilhas;
- módulos;
- desafios;
- tentativas.

