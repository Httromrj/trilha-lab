# Trilha Lab

Uma plataforma de trilhas práticas para aprender Python, SQL, IA, Machine Learning e Dados com desafios progressivos, exemplos reais reorganizados e laboratório seguro no estilo Colab.

Este projeto nasceu a partir de exemplos reais de estudo, corrigidos e reorganizados em uma experiência mais clara, progressiva e divertida. O TaxPilot entra apenas como referência de produto: a ideia de organizar informações, transformar dados em contexto e construir uma experiência assistida por IA.

## Destaques

- Lab local estilo Google Colab.
- Banco com 100+ desafios por trilha e seleção livre da quantidade para estudar.
- Execução contextual e mais segura para estudantes.
- Trilha do iniciante ao intermediário.
- Trilha SQL separada para consultas e modelagem.
- Catálogo de exemplos reais usados como referência.
- Estrutura pronta para virar repositório de portfólio no GitHub.

## Para quem é

- Pessoas iniciantes que já querem praticar desde o primeiro dia.
- Estudantes em nível intermediário que querem consolidar fundamentos.
- Quem quer montar um portfólio com pequenos desafios e um projeto final.

## Como estudar

1. Leia a visão geral em [`docs/visao-geral.md`](docs/visao-geral.md).
2. Siga os módulos em ordem, dentro da pasta [`modulos/`](modulos/).
3. Resolva os desafios em [`desafios/`](desafios/).
4. Rode os mini projetos em [`projetos/`](projetos/).
5. Use o projeto final para montar sua apresentação.

## Estrutura

```text
jornada-python-ia-dados/
├── .github/workflows/      # Automação de validação para GitHub Actions
├── assets/                 # Espaço para imagens, GIFs e vídeos
├── dados/                  # Bases simples para os labs
├── desafios/               # Pequenos desafios guiados
├── docs/                   # Orientações, roteiro e referências
├── materiais-originais/    # Backup dos exemplos usados como fonte
├── modulos/                # Aulas em ordem progressiva
├── projetos/               # Labs executáveis e incrementais
├── site/                   # Vitrine interativa com animações
├── src/                    # Scripts de apoio
└── requirements.txt
```

## Como ver e testar

```powershell
cd jornada-python-ia-dados
python src\start_jornada.py
```

Depois abra:

```text
http://127.0.0.1:8850
```

Esse servidor abre a trilha visual e o lab no mesmo endereço.

Página principal:

```text
http://127.0.0.1:8850
```

Lab:

```text
http://127.0.0.1:8850/lab
```

## Lab de execução

O lab fica em `http://127.0.0.1:8850/lab`.

Ele tem exemplos editáveis por tema e mostra a saída do Python em tempo real. Ele executa apenas recursos ligados ao contexto selecionado. Veja detalhes em [`docs/lab-execucao.md`](docs/lab-execucao.md).

## Desafios

O banco principal tem 100 desafios em [`desafios/100-desafios-python.md`](desafios/100-desafios-python.md). No lab, o aluno escolhe quantos desafios quer gerar naquele momento, usando esse banco como fonte.

## Trilha SQL

A trilha SQL fica separada em [`trilhas/sql`](trilhas/sql). Ela cobre fundamentos, filtros, agregações, joins, modelagem e uma visão futura para DBA com apoio de IA.

## Experiência visual

Abra a vitrine interativa pelo servidor local em `http://127.0.0.1:8850/site/index.html`.

Ideias de imagens, vídeos, GIFs e automações estão em [`docs/midia-e-automacoes.md`](docs/midia-e-automacoes.md).

## Exemplos originais

Veja como os arquivos de estudo foram mapeados na trilha em [`docs/catalogo-exemplos.md`](docs/catalogo-exemplos.md).

## Publicação no GitHub

Repositório oficial: [Httromrj/trilha-lab](https://github.com/Httromrj/trilha-lab).

Roteiro em [`docs/roadmap-github.md`](docs/roadmap-github.md) e pitch em [`docs/pitch.md`](docs/pitch.md).

## Redes sociais

- GitHub: [Httromrj](https://github.com/Httromrj)
- Demais links: ver [`docs/redes-sociais.md`](docs/redes-sociais.md) e [`dados/social_links.json`](dados/social_links.json)

## Principios do projeto

- Aprender construindo, não apenas lendo.
- Explicar conceitos com exemplos pequenos antes de juntar tudo.
- Transformar erros comuns de aprendizado em boas práticas.
- Manter os exemplos originais em backup, mas publicar a versão limpa.
- Usar IA com responsabilidade: como apoio, não como resposta mágica.

## Projeto final

O projeto final é um assistente educacional de organização de dados. Ele se inspira no TaxPilot, mas não copia nem altera o projeto original. O objetivo é treinar:

- leitura e limpeza de dados;
- modelagem simples de banco;
- prompts e fluxo de conversa;
- análise com pandas;
- primeiro modelo de Machine Learning;
- documentação de uma solução de IA.
