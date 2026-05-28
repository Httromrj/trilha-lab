# Roadmap para Publicar no GitHub

## Objetivo do repositório

Apresentar uma plataforma de trilhas práticas do iniciante ao intermediário, com:

- módulos progressivos;
- lab local estilo Colab;
- gerador de desafios por trilha e nível para Python, SQL, IA e Dados;
- exemplos reais reorganizados;
- projeto final inspirado pelo TaxPilot;
- documentação clara para portfólio.

## Estrutura recomendada

```text
jornada-python-ia-dados/
├── README.md
├── docs/
│   ├── visao-geral.md
│   ├── lab-execucao.md
│   ├── catalogo-exemplos.md
│   ├── pitch.md
│   └── roadmap-github.md
├── modulos/
├── desafios/
├── site/
├── src/
├── dados/
├── projetos/
└── materiais-originais/
```

## Antes de subir

- Usar o repositório final: `https://github.com/Httromrj/trilha-lab`.
- Atualizar redes sociais em `docs/redes-sociais.md`.
- Escolher uma imagem de capa para `assets/cover.png`.
- Revisar se os exemplos originais podem ficar publicados.
- Criar um vídeo curto demonstrando o lab.
- Rodar validação local.

## Trilhas no lab

O lab deve ser o ponto central para escolher:

- Python;
- SQL;
- IA;
- futuras trilhas, como DBA com IA.

Cada trilha precisa ter:

- banco mínimo de 100 desafios;
- níveis de dificuldade;
- dicas específicas;
- executor ou avaliador adequado ao tipo de exercício.

No momento, Python executa código local, SQL executa consultas seguras em SQLite e IA registra respostas para futura avaliação por rubrica/assistente.

## Comandos sugeridos

```powershell
python src\start_jornada.py
python src\explorador_dados.py
python src\ml_gorjetas.py
```

## Sugestão de descrição do GitHub

Trilhas interativas de Python, SQL, IA, Machine Learning e Dados com lab local estilo Colab, gerador de desafios e exemplos reais reorganizados.
