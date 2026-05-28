# 03 - Agregações

## Objetivo

Resumir dados com funções agregadoras.

## Funções

```sql
SELECT COUNT(*) FROM alunos;

SELECT AVG(pontos) FROM alunos;

SELECT MAX(pontos) FROM alunos;

SELECT MIN(pontos) FROM alunos;
```

## Agrupamento

```sql
SELECT trilha, COUNT(*) AS total
FROM alunos
GROUP BY trilha;
```

## Missão

Descubra:

- quantidade de alunos;
- média de pontos;
- maior pontuação;
- quantidade de alunos por trilha.

