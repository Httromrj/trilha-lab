# 04 - Joins

## Objetivo

Combinar dados de mais de uma tabela.

## Exemplo

```sql
SELECT alunos.nome, missoes.titulo, missoes.status
FROM alunos
JOIN missoes ON missoes.aluno_id = alunos.id;
```

## Tipos comuns

- `INNER JOIN`: traz registros com correspondência nas duas tabelas.
- `LEFT JOIN`: traz todos da tabela da esquerda e os correspondentes da direita.

## Missão

Modele duas tabelas:

- `alunos`
- `missoes`

Depois escreva uma consulta que mostre aluno, missão e status.

