# Projeto 05 - Assistente de IA Educacional

## Objetivo

Desenhar um assistente que organiza informações e devolve um resumo claro ao usuário.

## Inspiração

O TaxPilot serve apenas como referência de experiência: coletar dados, organizar contexto e orientar o próximo passo.

## Fluxo sugerido

1. Perguntar objetivo do usuário.
2. Coletar dados essenciais.
3. Validar campos ausentes.
4. Salvar em JSON ou SQLite.
5. Gerar um resumo.
6. Montar um prompt com contexto.
7. Avaliar se a resposta foi útil.

## Prompt base

```text
Você é um assistente educacional de dados.
Seu papel é organizar as informações recebidas, apontar campos faltantes
e sugerir próximos passos de estudo.
Não dê recomendações fiscais, financeiras ou jurídicas.

Contexto:
{contexto_do_usuario}

Tarefa:
Gere um resumo claro, uma lista de pendências e uma sugestão de próxima missão.
```

## Entrega

Crie um protótipo simples antes de pensar em interface bonita. Primeiro o fluxo precisa funcionar.

