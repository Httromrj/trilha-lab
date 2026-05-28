# Lab de Execução

O projeto agora tem um laboratório local para o aluno escrever e executar pequenos códigos Python no navegador.

## Como abrir

```powershell
python src\lab_execucao.py
```

Depois acesse:

```text
http://127.0.0.1:8850
```

## O que ele permite

- Escolher exemplos por tema.
- Manter um banco mínimo de 100 desafios por trilha, mas permitir que o aluno gere uma quantidade menor para testar ou estudar em blocos curtos.
- Editar o código no navegador.
- Executar e ver `print()`, erros e tracebacks.
- Testar rapidamente variações dos exercícios.

## Gerador por grau

O aluno escolhe:

- `Iniciante`: mais desafios de `print`, variáveis, `input`, strings, matemática e listas.
- `Intermediário`: mais funções, organização de código, pandas e análise de dados.
- `Revisão geral`: distribuição equilibrada entre fundamentos, coleções, funções e pandas.

O banco deve ter pelo menos 100 desafios por trilha, mas a sessão respeita a quantidade escolhida pelo aluno.

## Atalhos

- `Ctrl + Enter`: executa o código.
- `F9`: executa a célula atual.
- `Tab`: insere quatro espaços no editor.

## Segurança

Este lab executa código Python na máquina local. Ele foi feito para estudo individual e não deve ser publicado em servidor aberto na internet.

O modo padrão tem bloqueios básicos:

- bloqueia imports fora de uma lista permitida;
- bloqueia imports fora do contexto do exemplo atual;
- bloqueia `open`, `eval`, `exec`, `compile`, `input` e funções similares;
- bloqueia operações comuns de arquivo, como `unlink`, `remove`, `rmtree`, `write_text` e `write_bytes`;
- permite `pandas.read_csv` e `pandas.read_json` apenas com caminhos literais dentro de `dados/`;
- executa o código com timeout curto;
- limita o tamanho da saída.

Esses bloqueios ajudam no uso didático local, mas não são uma sandbox perfeita. Para uma versão pública, o ideal é usar um sandbox real, como ambiente isolado em container, execução no navegador com Pyodide ou serviço especializado de code runner.

## Contexto da aula

O lab não é um editor livre. Ele acompanha o que o aluno está vendo:

- em `Python Base`, o foco é variável, tipo, operador, string e `print`;
- em `Coleções`, entram listas, dicionários, `if` e laços;
- em `Funções`, entram `def`, retorno e reaproveitamento de código;
- em `Pandas`, entra `import pandas` e leitura controlada de arquivos em `dados/`.

Se o aluno tentar usar algo fora do tema atual, o lab bloqueia e mostra uma mensagem curta.

## Imports tecnicamente permitidos

- `collections`
- `datetime`
- `json`
- `math`
- `pathlib`
- `pandas`
- `random`
- `re`
- `statistics`

A liberação final depende do contexto atual. Por exemplo: `pandas` só é aceito no exemplo de pandas.

## Ideias de evolução

- Adicionar exercícios salvos por módulo.
- Mostrar testes automáticos para cada desafio.
- Criar pontuação quando o código passa nos testes.
- Salvar tentativas em JSON ou SQLite.
- Gerar certificado local de conclusão da trilha.
- Criar uma versão pública com Pyodide para executar Python direto no navegador.
