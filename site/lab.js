const pools = {
  "python-base": [
    "Imprima seu nome e sua idade",
    "Guarde seu nome em uma variável",
    "Peça o nome usando input",
    "Peça a idade usando input",
    "Some dois números",
    "Subtraia dois números",
    "Multiplique dois números",
    "Divida dois números",
    "Calcule o resto de uma divisão",
    "Converta texto para inteiro",
    "Converta texto para decimal",
    "Monte uma frase com f-string",
    "Transforme texto em maiúsculas",
    "Transforme texto em minúsculas",
    "Conte letras de um nome",
    "Calcule idade daqui a 5 anos",
    "Calcule desconto de um produto",
    "Calcule média de duas notas",
    "Compare dois números",
    "Verifique se a pessoa é maior de idade",
    "Mostre uma mensagem de boas-vindas",
    "Calcule preço com taxa",
    "Converta minutos em horas",
    "Calcule IMC simples",
    "Arredonde um número decimal"
  ],
  colecoes: [
    "Crie uma lista de linguagens",
    "Acesse o primeiro item da lista",
    "Adicione item com append",
    "Remova item da lista",
    "Conte itens com len",
    "Percorra lista com for",
    "Some valores de uma lista",
    "Encontre o maior valor",
    "Encontre o menor valor",
    "Filtre números pares",
    "Filtre números acima de 10",
    "Crie uma tupla de módulos",
    "Crie um set sem repetição",
    "Verifique item com in",
    "Crie um dicionário de aluno",
    "Leia valor de um dicionário",
    "Atualize status no dicionário",
    "Percorra chaves e valores",
    "Crie lista de dicionários",
    "Conte categorias únicas",
    "Crie menu simples com if",
    "Crie while com contador",
    "Crie tabuada com for",
    "Crie ranking de pontuações",
    "Crie resumo de gastos"
  ],
  funcoes: [
    "Crie função sem parâmetro",
    "Crie função com nome",
    "Crie função de soma",
    "Crie função de média",
    "Retorne percentual",
    "Valide texto vazio",
    "Valide número positivo",
    "Calcule desconto com função",
    "Formate mensagem com função",
    "Use valor padrão em função",
    "Liste pares com função",
    "Retorne maior valor",
    "Retorne menor valor",
    "Receba lista em função",
    "Devolva dicionário em função",
    "Separe regra de apresentação",
    "Reutilize função duas vezes",
    "Crie função de status",
    "Crie função de pontuação",
    "Crie mini calculadora",
    "Crie função de progresso",
    "Classifique idade",
    "Limpe texto com função",
    "Gere relatório com função",
    "Resolva desafio final com função"
  ],
  pandas: [
    "Leia CSV de gorjetas",
    "Mostre primeiras linhas",
    "Veja colunas do DataFrame",
    "Conte linhas e colunas",
    "Calcule média da conta",
    "Calcule média da gorjeta",
    "Encontre maior gorjeta",
    "Encontre menor conta",
    "Filtre contas acima de 20",
    "Crie coluna percentual",
    "Agrupe gorjeta por dia",
    "Ordene valores",
    "Selecione colunas",
    "Use describe",
    "Verifique nulos",
    "Conte valores por dia",
    "Compare almoço e jantar",
    "Filtre por tamanho da mesa",
    "Calcule total por dia",
    "Crie resumo textual",
    "Prepare X e y",
    "Preveja gorjeta manualmente",
    "Detecte valor acima da média",
    "Crie relatório final",
    "Explique uma descoberta"
  ]
};

const distributions = {
  iniciante: [["python-base", 55], ["colecoes", 30], ["funcoes", 15], ["pandas", 0]],
  intermediario: [["python-base", 15], ["colecoes", 25], ["funcoes", 25], ["pandas", 35]],
  geral: [["python-base", 25], ["colecoes", 25], ["funcoes", 25], ["pandas", 25]]
};

const sqlLessonPlan = [
  {
    lesson: "01 - Conhecer tabelas",
    context: "sql-select-all",
    tasks: [
      "Selecione todos os campos da tabela alunos",
      "Selecione todos os campos da tabela missoes"
    ]
  },
  {
    lesson: "02 - Escolher colunas",
    context: "sql-select-columns",
    tasks: [
      "Mostre apenas nome e trilha da tabela alunos",
      "Mostre apenas cidade e pontos da tabela alunos",
      "Mostre apenas titulo e status da tabela missoes",
      "Mostre apenas aluno_id e pontos da tabela missoes",
      "Mostre nome, cidade e trilha da tabela alunos",
      "Mostre titulo, status e pontos da tabela missoes",
      "Mostre a coluna nome com alias aluno",
      "Mostre a coluna titulo com alias missao",
      "Mostre pontos da tabela alunos com alias pontuacao",
      "Mostre status da tabela missoes com alias situacao"
    ]
  },
  {
    lesson: "03 - Organizar resultados",
    context: "sql-order-limit",
    tasks: [
      "Ordene alunos por nome em ordem crescente",
      "Ordene alunos por pontos em ordem decrescente",
      "Ordene missoes por titulo em ordem crescente",
      "Ordene missoes por pontos em ordem decrescente",
      "Mostre os 2 primeiros alunos",
      "Mostre as 2 primeiras missoes",
      "Mostre os 3 alunos com maior pontuacao",
      "Mostre as 3 missoes com menor pontuacao",
      "Ordene alunos por trilha e depois por nome",
      "Ordene missoes por status e depois por titulo"
    ]
  },
  {
    lesson: "04 - Filtrar com WHERE",
    context: "sql-filter",
    tasks: [
      "Filtre alunos da trilha Python",
      "Filtre alunos da cidade Sao Paulo",
      "Filtre alunos com mais de 50 pontos",
      "Filtre alunos com pontos menores que 70",
      "Filtre missoes pendentes",
      "Filtre missoes concluidas",
      "Filtre missoes com 15 pontos",
      "Filtre alunos cujo nome seja Ana",
      "Filtre alunos com trilha diferente de SQL",
      "Filtre missoes do aluno_id 1",
      "Use LIKE para buscar alunos com nome iniciado por C",
      "Use LIKE para buscar missoes com a palavra SELECT",
      "Use IN para filtrar trilhas Python e Dados",
      "Use IN para filtrar status pendente e concluida",
      "Use BETWEEN para alunos entre 50 e 80 pontos",
      "Use BETWEEN para missoes entre 10 e 20 pontos",
      "Use AND para alunos da trilha Python com mais de 70 pontos",
      "Use OR para alunos de Sao Paulo ou Salvador"
    ]
  },
  {
    lesson: "05 - Resumir com agregacoes",
    context: "sql-aggregate",
    tasks: [
      "Conte todos os alunos",
      "Conte todas as missoes",
      "Calcule a media de pontos dos alunos",
      "Calcule a media de pontos das missoes",
      "Encontre a maior pontuacao dos alunos",
      "Encontre a menor pontuacao dos alunos",
      "Some os pontos das missoes",
      "Some os pontos dos alunos",
      "Conte alunos por trilha",
      "Conte alunos por cidade",
      "Conte missoes por status",
      "Some pontos de missoes por status",
      "Calcule media de pontos por trilha",
      "Encontre maior pontuacao por cidade",
      "Agrupe missoes por aluno_id",
      "Filtre grupos com HAVING para trilhas com pelo menos 1 aluno"
    ]
  },
  {
    lesson: "06 - Relacionar tabelas com JOIN",
    context: "sql-join",
    tasks: [
      "Relacione alunos e missoes com JOIN",
      "Liste nome do aluno e titulo da missao",
      "Liste nome do aluno, trilha e status da missao",
      "Liste missoes pendentes com nome do aluno",
      "Liste missoes concluidas com nome do aluno",
      "Liste pontos da missao com a trilha do aluno",
      "Filtre JOIN para alunos da trilha Python",
      "Filtre JOIN para missoes com mais de 10 pontos",
      "Ordene JOIN por nome do aluno",
      "Ordene JOIN por pontos da missao",
      "Use alias al e mi no JOIN",
      "Mostre nome do aluno com alias aluno e titulo com alias missao",
      "Conte missoes por aluno",
      "Some pontos de missoes por aluno",
      "Calcule media de pontos de missoes por trilha",
      "Liste alunos e missoes usando WHERE no JOIN",
      "Liste nome, cidade, titulo e status",
      "Liste apenas alunos que possuem missoes pendentes",
      "Liste apenas alunos que possuem missoes concluidas",
      "Crie uma consulta final combinando JOIN, WHERE e ORDER BY"
    ]
  },
  {
    lesson: "07 - Revisao guiada",
    context: "sql-filter",
    tasks: [
      "Revise SELECT escolhendo colunas e filtrando alunos",
      "Revise WHERE com texto entre aspas simples",
      "Revise ORDER BY em uma consulta filtrada",
      "Revise LIMIT para mostrar poucos resultados",
      "Revise IN com duas trilhas",
      "Revise BETWEEN com pontos de alunos",
      "Revise LIKE com nomes",
      "Revise filtros em missoes"
    ]
  },
  {
    lesson: "08 - Revisao com dados resumidos",
    context: "sql-aggregate",
    tasks: [
      "Revise COUNT por status de missao",
      "Revise AVG por trilha",
      "Revise SUM por aluno_id",
      "Revise MAX por cidade",
      "Revise MIN por status",
      "Revise GROUP BY por trilha",
      "Revise HAVING com contagem",
      "Revise agregacao com alias"
    ]
  },
  {
    lesson: "09 - Revisao com relacionamento",
    context: "sql-join",
    tasks: [
      "Revise JOIN entre alunos e missoes",
      "Revise JOIN com alias",
      "Revise JOIN com filtro por status",
      "Revise JOIN com filtro por trilha",
      "Revise JOIN com ORDER BY",
      "Revise JOIN com agregacao por aluno",
      "Revise JOIN com soma por trilha",
      "Monte uma consulta final de portfolio"
    ]
  }
];

const sqlPools = Object.fromEntries(
  sqlLessonPlan.map((lesson) => [lesson.context, lesson.tasks])
);

const iaPools = {
  "ia-base": [
    "Explique o que é IA em uma frase",
    "Crie um prompt para pedir ajuda em Python",
    "Crie um prompt com contexto do aluno",
    "Liste limites de um assistente de IA",
    "Identifique uma pergunta fora de escopo",
    "Transforme dados em contexto",
    "Crie resposta segura para dúvida fiscal",
    "Monte prompt para resumir CSV",
    "Monte prompt para revisar SQL",
    "Crie checklist de qualidade da resposta",
    "Compare prompt vago e prompt específico",
    "Escreva instruções do assistente",
    "Defina persona educacional",
    "Defina dados que não devem ser expostos",
    "Crie exemplo de fallback",
    "Crie métrica simples de utilidade",
    "Crie teste de resposta ruim",
    "Crie teste de resposta boa",
    "Simule conversa curta",
    "Explique alucinação de IA",
    "Crie prompt para gerar exercícios",
    "Crie prompt para explicar erro",
    "Crie prompt para não dar resposta pronta",
    "Crie rubrica de avaliação",
    "Crie plano de melhoria do assistente"
  ]
};

const trackConfigs = {
  python: {
    label: "Python",
    pools,
    distributions,
  },
  sql: {
    label: "SQL",
    pools: sqlPools,
    distributions: {
      iniciante: [["sql-select-all", 12], ["sql-select-columns", 18], ["sql-order-limit", 15], ["sql-filter", 25], ["sql-aggregate", 18], ["sql-join", 12]],
      intermediario: [["sql-select-all", 5], ["sql-select-columns", 10], ["sql-order-limit", 15], ["sql-filter", 25], ["sql-aggregate", 25], ["sql-join", 20]],
      geral: [["sql-select-all", 10], ["sql-select-columns", 15], ["sql-order-limit", 15], ["sql-filter", 20], ["sql-aggregate", 20], ["sql-join", 20]],
    },
  },
  ia: {
    label: "IA",
    pools: iaPools,
    distributions: {
      iniciante: [["ia-base", 100]],
      intermediario: [["ia-base", 100]],
      geral: [["ia-base", 100]],
    },
  },
};

let challenges = [];
let currentIndex = 0;
let baseConfigSummary = "Python - Iniciante - 10 desafios";
let solvedChallenges = new Set();
let highestUnlockedIndex = 0;
let appendMode = false;

const trackSelect = document.querySelector("#trackSelect");
const level = document.querySelector("#studentLevel");
const amount = document.querySelector("#challengeAmount");
const number = document.querySelector("#challengeNumber");
const title = document.querySelector("#questionTitle");
const instruction = document.querySelector("#questionInstruction");
const tipsList = document.querySelector("#tipsList");
const context = document.querySelector("#currentContext");
const code = document.querySelector("#codeInput");
const codeNotes = document.querySelector("#codeNotes");
const stdin = document.querySelector("#stdinInput");
const inputPanel = document.querySelector(".input-panel");
const output = document.querySelector("#output");
const feedback = document.querySelector("#runFeedback");
const list = document.querySelector("#challengeList");
const search = document.querySelector("#challengeSearch");
const autocomplete = document.querySelector("#autocomplete");
const generateStatus = document.querySelector("#generateStatus");
const generateButton = document.querySelector("#generateChallenges");
const drawer = document.querySelector("#challengeDrawer");
const settingsDrawer = document.querySelector("#settingsDrawer");
const progressText = document.querySelector("#progressText");
const progressEstimate = document.querySelector("#progressEstimate");
const progressFill = document.querySelector("#progressFill");
const labConfigSummary = document.querySelector("#labConfigSummary");
const completionPanel = document.querySelector("#completionPanel");
const completionText = document.querySelector("#completionText");
const baseSuggestions = ["print()", "input()", "int()", "float()", "str()", "len()", "sum()", "range()", "for", "if", "def", "return", "pd.read_csv()"];
const sqlSuggestions = {
  "sql-select-all": ["SELECT", "*", "FROM", "alunos", "missoes"],
  "sql-select-columns": ["SELECT", "FROM", "AS", "alunos", "missoes", "nome", "trilha", "titulo", "status", "pontos"],
  "sql-order-limit": ["SELECT", "FROM", "ORDER BY", "ASC", "DESC", "LIMIT", "alunos", "missoes"],
  "sql-filter": ["SELECT", "FROM", "WHERE", "LIKE", "IN", "BETWEEN", "AND", "OR", "alunos", "missoes"],
  "sql-aggregate": ["SELECT", "FROM", "COUNT()", "AVG()", "SUM()", "MIN()", "MAX()", "GROUP BY", "alunos", "missoes"],
  "sql-join": ["SELECT", "FROM", "JOIN", "ON", "WHERE", "alunos", "missoes", "aluno_id"]
};

function makeChallenge(id, text, ctx, round = 1) {
  const suffix = round > 1 ? ` (variação ${round})` : "";
  return {
    id,
    title: `${text}${suffix}`,
    context: ctx,
    instruction: instructionFor(text, ctx),
    tips: tipsFor(text, ctx),
    starter: starterFor(text, ctx),
    stdin: stdinFor(text),
    lesson: ""
  };
}

function makeChallengeFromSpec(id, spec, round = 1) {
  const suffix = round > 1 ? ` (revisao ${round})` : "";
  return {
    id,
    title: `${spec.title}${suffix}`,
    context: spec.context,
    instruction: spec.instruction || instructionFor(spec.title, spec.context),
    tips: spec.tips || tipsFor(spec.title, spec.context),
    starter: spec.starter || starterFor(spec.title, spec.context),
    stdin: "",
    lesson: spec.lesson
  };
}

function buildSqlChallenges(total) {
  const orderedSpecs = sqlLessonPlan.flatMap((lesson) =>
    lesson.tasks.map((title) => ({
      title,
      context: lesson.context,
      lesson: lesson.lesson
    }))
  );

  const generated = [];
  for (let index = 0; generated.length < total; index += 1) {
    const spec = orderedSpecs[index % orderedSpecs.length];
    const round = Math.floor(index / orderedSpecs.length) + 1;
    generated.push(makeChallengeFromSpec(generated.length + 1, spec, round));
  }
  return generated;
}

function buildChallenges(total) {
  const track = trackConfigs[trackSelect.value] || trackConfigs.python;

  if (trackSelect.value === "sql") {
    return buildSqlChallenges(total);
  }

  const generated = [];
  const dist = track.distributions[level.value] || track.distributions.iniciante;

  dist.forEach(([ctx, percent]) => {
    const target = Math.round((total * percent) / 100);
    for (let i = 0; i < target; i += 1) {
      const source = track.pools[ctx];
      generated.push(makeChallenge(generated.length + 1, source[i % source.length], ctx, Math.floor(i / source.length) + 1));
    }
  });

  while (generated.length < total) {
    const fallbackContext = Object.keys(track.pools)[0];
    const fallbackPool = track.pools[fallbackContext];
    generated.push(makeChallenge(generated.length + 1, fallbackPool[generated.length % fallbackPool.length], fallbackContext));
  }

  return generated;
}

function generateChallenges(options = {}) {
  const requested = Number(amount.value) || 100;
  const total = Math.max(1, Math.min(requested, 100));
  amount.value = total;
  const track = trackConfigs[trackSelect.value] || trackConfigs.python;

  if (options.append && challenges.length) {
    const startIndex = challenges.length;
    const expanded = buildChallenges(startIndex + total);
    const additions = expanded.slice(startIndex);

    challenges = [...challenges, ...additions];
    currentIndex = startIndex;
    highestUnlockedIndex = Math.max(highestUnlockedIndex, startIndex);
    completionPanel.hidden = true;
    baseConfigSummary = `${track.label} - ${level.options[level.selectedIndex].textContent} - ${challenges.length} desafios`;
    labConfigSummary.textContent = baseConfigSummary;
    generateStatus.textContent = `${additions.length} novos desafios adicionados. Total da sessao: ${challenges.length}`;
    generateStatus.classList.remove("warn");
    renderList();
    loadChallenge(currentIndex);
    return;
  }

  const generated = buildChallenges(total);

  challenges = generated;
  currentIndex = 0;
  solvedChallenges = new Set();
  highestUnlockedIndex = 0;
  completionPanel.hidden = true;
  baseConfigSummary = `${track.label} - ${level.options[level.selectedIndex].textContent} - ${total} desafios`;
  labConfigSummary.textContent = baseConfigSummary;
  generateStatus.textContent = requested > 100
    ? "limite aplicado: 100 desafios"
    : `${total} desafios de ${track.label} gerados`;
  generateStatus.classList.toggle("warn", requested > 100);
  renderList();
  loadChallenge(0);
}

function instructionFor(text, ctx) {
  if (ctx === "sql-select-all") return "Use apenas SELECT, * e FROM. Filtros, ordenacao e JOIN entram depois.";
  if (ctx === "sql-select-columns") return "Escolha colunas especificas com SELECT e FROM. Ainda nao use WHERE, ORDER BY ou JOIN.";
  if (ctx === "sql-order-limit") return "Use SELECT e FROM com ORDER BY ou LIMIT. Ainda nao use filtros ou JOIN.";
  if (ctx === "sql-filter") return "Use WHERE para filtrar resultados. JOIN e agrupamentos ficam para etapas futuras.";
  if (ctx === "sql-aggregate") return "Use funcoes de agregacao como COUNT, AVG, SUM, MIN ou MAX. JOIN fica para a proxima etapa.";
  if (ctx === "sql-join") return "Use JOIN para relacionar alunos e missoes.";
  if (ctx === "ia-base") return "Escreva um prompt, uma explicação ou uma resposta curta. O foco é usar IA com contexto e segurança.";
  if (text.includes("Imprima seu nome")) return "Use print() para mostrar seu nome e sua idade na tela.";
  if (text.includes("input")) return "Use input() para receber dados. Preencha a entrada simulada antes de executar.";
  if (ctx === "python-base") return "Resolva usando apenas recursos básicos: variável, operador, string, conversão e print.";
  if (ctx === "colecoes") return "Resolva usando listas, dicionários, sets, if, for ou while.";
  if (ctx === "funcoes") return "Resolva criando uma função pequena e chamando essa função no final.";
  return "Use pandas com dados/relatorio_gorjetas.csv. O lab só permite leitura dentro da pasta dados/.";
}

function tipsFor(text, ctx) {
  if (ctx.startsWith("sql-")) return sqlTipsFor(text, ctx);
  if (ctx === "ia-base") return ["Dê contexto antes da tarefa.", "Diga o formato esperado da resposta.", "Inclua limites do assistente."];
  if (text.includes("Imprima seu nome")) return ["Use print para mostrar texto.", "Texto em Python fica entre aspas.", "Número pode ser escrito diretamente."];
  if (text.includes("input")) return ["input() sempre retorna texto.", "Use int(input(...)) quando precisar fazer conta.", "Preencha a entrada simulada abaixo da célula."];
  if (ctx === "python-base") return ["Comece criando variáveis.", "Use print() para conferir o resultado.", "Teste uma linha por vez."];
  if (ctx === "colecoes") return ["Crie a lista primeiro.", "Use for para percorrer.", "Use if para filtrar."];
  if (ctx === "funcoes") return ["Defina com def.", "Use return para devolver valor.", "Chame a função no final."];
  return ["Importe pandas como pd.", "Leia dados/relatorio_gorjetas.csv.", "Use head(), mean(), groupby() ou shape."];
}

function sqlTipsFor(text, ctx) {
  const table = text.toLowerCase().includes("miss") ? "missoes" : "alunos";

  if (ctx === "sql-select-all") {
    return [
      `A tabela pedida e ${table}.`,
      `Use exatamente SELECT * FROM ${table};`,
      "Nao use filtros, ordenacao ou JOIN nesta primeira etapa."
    ];
  }

  if (ctx === "sql-select-columns") {
    const columns = text.match(/nome|trilha|cidade|pontos|titulo|status|aluno_id|alias|pontuacao|situacao/gi)?.join(", ") || "as colunas pedidas";
    return [
      `A consulta deve usar a tabela ${table}.`,
      `Troque * por ${columns}.`,
      "Se o enunciado pedir alias, use AS para dar outro nome a coluna."
    ];
  }

  if (ctx === "sql-order-limit") {
    return [
      text.toLowerCase().includes("primeir") ? "Use LIMIT para reduzir a quantidade de linhas." : "Use ORDER BY para organizar o resultado.",
      text.toLowerCase().includes("decrescente") || text.toLowerCase().includes("maior") ? "DESC coloca os maiores valores primeiro." : "ASC e a ordem crescente padrao.",
      "Nesta etapa, use uma tabela por vez."
    ];
  }

  if (ctx === "sql-filter") {
    return [
      "A condicao vem depois de WHERE.",
      text.toLowerCase().includes("like") ? "LIKE usa padroes, por exemplo 'C%' para comecar com C." : "Texto em SQL fica entre aspas simples.",
      text.toLowerCase().includes("between") ? "BETWEEN recebe limite inicial e final." : "Comece filtrando uma regra simples."
    ];
  }

  if (ctx === "sql-aggregate") {
    return [
      "Agregacoes resumem varias linhas em um resultado.",
      text.toLowerCase().includes("por ") || text.toLowerCase().includes("grupo") ? "Quando o enunciado pede 'por categoria', use GROUP BY." : "COUNT, AVG, SUM, MIN e MAX sao as funcoes desta etapa.",
      text.toLowerCase().includes("having") ? "HAVING filtra grupos depois do GROUP BY." : "Use alias com AS se quiser deixar a saida mais legivel."
    ];
  }

  return [
    "JOIN combina linhas de duas tabelas.",
    "A relacao deste lab e alunos.id = missoes.aluno_id.",
    text.toLowerCase().includes("alias") ? "Alias como al e mi deixam a consulta mais curta." : "Comece selecionando poucas colunas para conferir a relacao."
  ];
}

function starterFor(text, ctx) {
  if (ctx.startsWith("sql-")) {
    if (ctx === "sql-select-all") {
      return "-- Escreva sua consulta SQL abaixo.\n-- Nesta etapa use apenas: SELECT * FROM tabela;\n\nSELECT *\nFROM ;";
    }
    return "-- Escreva sua consulta SQL abaixo.\n-- Tabelas: alunos, missoes\n\nSELECT \nFROM ;";
  }
  if (ctx === "ia-base") {
    return "# Escreva seu prompt ou resposta abaixo.\n# Inclua contexto, tarefa e limite.\n\n";
  }
  if (text.includes("Imprima seu nome")) {
    return "# Escreva sua resposta abaixo.\n# Mostre seu nome e sua idade usando print().\n# Dica: texto precisa ficar entre aspas.\n\n";
  }
  if (text.includes("Guarde seu nome")) {
    return "# Crie uma variável para guardar seu nome.\n# Depois mostre essa variável com print().\n\n";
  }
  if (text.includes("Peça o nome")) {
    return "# Peça o nome com input().\n# Depois mostre o valor recebido.\n\n";
  }
  if (text.includes("Peça a idade")) {
    return "# Peça a idade com input().\n# Se quiser fazer conta, converta para int().\n\n";
  }
  if (text.includes("Some")) {
    return "# Crie dois números, some e mostre o resultado.\n\n";
  }
  if (ctx === "python-base") {
    return "# Escreva sua solução abaixo.\n# Use apenas variáveis, operadores, strings, conversões e print.\n\n";
  }
  if (ctx === "colecoes") {
    return "# Escreva sua solução abaixo.\n# Use listas, dicionários, if, for ou while.\n\n";
  }
  if (ctx === "funcoes") {
    return "# Escreva sua solução abaixo.\n# Crie uma função e chame essa função no final.\n\n";
  }
  return "# Escreva sua solução abaixo.\n# Use pandas e leia dados/relatorio_gorjetas.csv.\n\nimport pandas as pd\n\ndf = pd.read_csv(\"dados/relatorio_gorjetas.csv\")\n";
}

function stdinFor(text) {
  if (text.includes("Peça o nome")) return "Romulo\n";
  if (text.includes("Peça a idade")) return "30\n";
  return "";
}

function renderList() {
  const query = search.value.toLowerCase();
  let visibleLesson = "";
  list.innerHTML = "";
  challenges
    .filter((item) => `${item.id} ${item.title} ${item.context} ${item.lesson}`.toLowerCase().includes(query))
    .slice(0, 120)
    .forEach((item) => {
      if (item.lesson && item.lesson !== visibleLesson) {
        visibleLesson = item.lesson;
        const section = document.createElement("div");
        section.className = "challenge-section";
        section.textContent = item.lesson;
        list.appendChild(section);
      }

      const button = document.createElement("button");
      button.type = "button";
      button.className = "challenge-item";
      if (item.id === challenges[currentIndex]?.id) button.classList.add("active");
      if (challenges.findIndex((challenge) => challenge.id === item.id) > highestUnlockedIndex) {
        button.disabled = true;
      }
      button.textContent = `${String(item.id).padStart(3, "0")} - ${item.title}`;
      button.addEventListener("click", () => {
        loadChallenge(challenges.findIndex((challenge) => challenge.id === item.id));
        closeDrawer();
      });
      list.appendChild(button);
    });
}

function loadChallenge(index) {
  if (index > highestUnlockedIndex) {
    showFeedback(false, "Resolva o desafio atual antes de avançar para os próximos.");
    return;
  }

  currentIndex = Math.max(0, Math.min(index, challenges.length - 1));
  const item = challenges[currentIndex];
  const starter = splitStarter(item.starter, item.context);
  number.textContent = `Questão ${String(item.id).padStart(3, "0")}`;
  labConfigSummary.textContent = item.lesson ? `SQL - ${item.lesson}` : baseConfigSummary;
  title.textContent = item.title;
  instruction.textContent = item.lesson ? `${item.lesson}. ${item.instruction}` : item.instruction;
  context.textContent = item.context;
  code.value = starter.code;
  renderCodeNotes(starter.notes);
  stdin.value = item.stdin;
  inputPanel.hidden = !item.title.toLowerCase().includes("input");
  output.textContent = "A saída aparece aqui depois de executar.";
  output.classList.remove("error");
  feedback.hidden = true;
  feedback.className = "run-feedback";
  tipsList.innerHTML = item.tips.map((tip) => `<li>${tip}</li>`).join("");
  updateProgress();
  updateNavigation();
  renderList();
  code.focus();
}

function splitStarter(starter, ctx) {
  const commentPrefix = ctx.startsWith("sql-") ? "--" : "#";
  const notes = [];
  const codeLines = [];
  let collectingNotes = true;

  starter.split("\n").forEach((line) => {
    const trimmed = line.trim();
    if (collectingNotes && (trimmed.startsWith(commentPrefix) || trimmed === "")) {
      if (trimmed.startsWith(commentPrefix)) {
        notes.push(trimmed.replace(commentPrefix, "").trim());
      }
      return;
    }

    collectingNotes = false;
    codeLines.push(line);
  });

  return { notes, code: codeLines.join("\n").replace(/^\n+/, "") };
}

function renderCodeNotes(notes) {
  codeNotes.innerHTML = "";
  if (!notes.length) {
    codeNotes.classList.remove("visible");
    return;
  }

  notes.forEach((note) => {
    const line = document.createElement("div");
    line.textContent = note;
    codeNotes.appendChild(line);
  });
  codeNotes.classList.add("visible");
}

function openDrawer() {
  drawer.classList.add("open");
  drawer.setAttribute("aria-hidden", "false");
  search.focus();
}

function closeDrawer() {
  drawer.classList.remove("open");
  drawer.setAttribute("aria-hidden", "true");
}

function openSettings() {
  settingsDrawer.classList.add("open");
  settingsDrawer.setAttribute("aria-hidden", "false");
  trackSelect.focus();
}

function closeSettings() {
  settingsDrawer.classList.remove("open");
  settingsDrawer.setAttribute("aria-hidden", "true");
}

async function runCode() {
  const item = challenges[currentIndex];
  output.textContent = "Executando...";
  output.classList.remove("error");
  feedback.hidden = true;
  feedback.className = "run-feedback";
  const response = await fetch("/api/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code: code.value, context: item.context, stdin: stdin.value })
  });
  const result = await response.json();
  output.textContent = result.output || "(sem saída)";
  if (!result.ok) {
    output.classList.add("error");
    showFeedback(false, "Ainda não deu certo. Leia a mensagem de erro, ajuste a resposta e execute novamente.");
    updateNavigation();
    return;
  }

  const check = evaluateAnswer(item, result);
  if (!check.ok) {
    showFeedback(false, check.message);
    updateNavigation();
    return;
  }

  solvedChallenges.add(item.id);
  highestUnlockedIndex = Math.max(highestUnlockedIndex, currentIndex + 1);
  showFeedback(true, check.message);
  updateProgress();
  updateNavigation();
  renderList();
}

function showFeedback(ok, message) {
  feedback.hidden = false;
  feedback.className = `run-feedback ${ok ? "success" : "error"}`;
  feedback.textContent = message;
}

function updateNavigation() {
  const solved = solvedChallenges.has(challenges[currentIndex]?.id);
  document.querySelector("#nextChallenge").disabled = currentIndex >= challenges.length - 1 || !solved;
  document.querySelector("#previousChallenge").disabled = currentIndex <= 0;
}

function updateProgress() {
  const solvedCount = solvedChallenges.size;
  const percent = challenges.length ? Math.round((solvedCount / challenges.length) * 100) : 0;
  progressText.textContent = `${currentIndex + 1} de ${challenges.length}`;
  progressEstimate.textContent = `${percent}% concluido`;
  progressFill.style.width = `${percent}%`;
  renderCompletion();
}

function renderCompletion() {
  const finished = challenges.length > 0 && solvedChallenges.size === challenges.length;
  completionPanel.hidden = !finished;

  if (finished) {
    const label = challenges.length === 1 ? "desafio" : "desafios";
    completionText.textContent = `Voce concluiu ${challenges.length} ${label}. Continue praticando ou explore a trilha completa para ver o proximo assunto.`;
  }
}

function evaluateAnswer(item, result) {
  if (item.context.startsWith("sql-")) {
    return evaluateSqlAnswer(item, code.value);
  }

  if (item.context === "ia-base") {
    return code.value.trim().length >= 40
      ? { ok: true, message: "Resposta registrada. Boa: ela tem contexto suficiente para avaliação." }
      : { ok: false, message: "Escreva um pouco mais de contexto antes de avançar." };
  }

  return evaluatePythonAnswer(item, result);
}

function evaluatePythonAnswer(item, result) {
  const source = code.value.toLowerCase();
  const answer = (result.output || "").trim();
  const text = item.title.toLowerCase();

  if (!answer) {
    return { ok: false, message: "O código rodou, mas não mostrou saída. Use print() para exibir o resultado." };
  }

  if (text.includes("input") && !source.includes("input(")) {
    return { ok: false, message: "Este desafio pede input(). Use input() para receber o valor antes de mostrar o resultado." };
  }

  if (text.includes("variável") && !source.includes("=")) {
    return { ok: false, message: "Este desafio pede variável. Guarde o valor em uma variável antes de usar print()." };
  }

  if ((text.includes("some") || text.includes("subtraia") || text.includes("multiplique") || text.includes("divida")) && !/[+\-*/]/.test(source)) {
    return { ok: false, message: "Este desafio pede uma operação matemática. Use o operador correspondente antes do print()." };
  }

  if (!source.includes("print(")) {
    return { ok: false, message: "O resultado precisa aparecer na tela. Use print() para mostrar sua resposta." };
  }

  return { ok: true, message: "Resposta aceita. Agora você pode avançar para o próximo desafio." };
}

function evaluateSqlAnswer(item, source) {
  const sql = normalizeSql(source);
  const titleText = item.title.toLowerCase();

  if (item.context === "sql-select-all") {
    const table = titleText.includes("missoes") ? "missoes" : "alunos";
    return sql === `select * from ${table}`
      ? { ok: true, message: "Consulta correta. Você selecionou todos os campos da tabela pedida." }
      : { ok: false, message: `Para este desafio, use exatamente: SELECT * FROM ${table};` };
  }

  if (item.context === "sql-select-columns") {
    if (sql.includes(" * ")) return { ok: false, message: "Agora o objetivo é escolher colunas. Troque * pelos nomes pedidos." };
    if (!sql.startsWith("select ") || !sql.includes(" from ")) return { ok: false, message: "Use a estrutura SELECT coluna FROM tabela." };
    if (!containsExpectedTable(sql, titleText)) return { ok: false, message: "Confira a tabela pedida no enunciado: alunos ou missoes." };
    if (titleText.includes("alias") && !sql.includes(" as ")) return { ok: false, message: "O enunciado pede alias. Use AS para renomear a coluna." };
    return { ok: true, message: "Resposta aceita. Você escolheu colunas sem pular para filtros ou JOIN." };
  }

  if (item.context === "sql-order-limit") {
    if (titleText.includes("primeir") && !sql.includes(" limit ")) return { ok: false, message: "Este desafio pede poucos registros. Use LIMIT." };
    if (!titleText.includes("primeir") && !sql.includes(" order by ")) return { ok: false, message: "Este desafio pede ordenação. Use ORDER BY." };
    if ((titleText.includes("decrescente") || titleText.includes("maior")) && !sql.includes(" desc")) return { ok: false, message: "Para maior/decrescente, use DESC." };
    return { ok: true, message: "Resposta aceita. Você organizou a consulta dentro da etapa atual." };
  }

  if (item.context === "sql-filter") {
    if (!sql.includes(" where ")) return { ok: false, message: "Este desafio pede filtro. Use WHERE para criar a condição." };
    if (titleText.includes("like") && !sql.includes(" like ")) return { ok: false, message: "Este desafio pede LIKE. Use LIKE no filtro." };
    if (titleText.includes(" in ") && !sql.includes(" in ")) return { ok: false, message: "Este desafio pede IN. Use IN com a lista de valores." };
    if (titleText.includes("between") && !sql.includes(" between ")) return { ok: false, message: "Este desafio pede BETWEEN. Use BETWEEN com dois limites." };
    return { ok: true, message: "Resposta aceita. O filtro está no nível certo da trilha." };
  }

  if (item.context === "sql-aggregate") {
    if (!/\b(count|avg|sum|min|max)\s*\(/.test(sql)) return { ok: false, message: "Este desafio pede resumo. Use COUNT, AVG, SUM, MIN ou MAX." };
    if ((titleText.includes("por ") || titleText.includes("grupo")) && !sql.includes(" group by ")) return { ok: false, message: "Quando o enunciado pede 'por', use GROUP BY." };
    if (titleText.includes("having") && !sql.includes(" having ")) return { ok: false, message: "Este desafio pede HAVING para filtrar grupos." };
    return { ok: true, message: "Resposta aceita. Você resumiu os dados com agregação." };
  }

  if (!sql.includes(" join ") || !sql.includes(" on ")) {
    return { ok: false, message: "Este desafio pede relacionamento. Use JOIN com ON." };
  }
  if (titleText.includes("alias") && !(sql.includes(" alunos al") || sql.includes(" missoes mi"))) {
    return { ok: false, message: "O enunciado pede alias. Use alunos al e/ou missoes mi." };
  }
  return { ok: true, message: "Resposta aceita. Você relacionou as tabelas com JOIN." };
}

function normalizeSql(source) {
  return source
    .split("\n")
    .filter((line) => !line.trim().startsWith("--"))
    .join(" ")
    .replace(/;/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();
}

function containsExpectedTable(sql, titleText) {
  if (titleText.includes("miss")) return sql.includes(" from missoes");
  if (titleText.includes("aluno")) return sql.includes(" from alunos");
  return sql.includes(" from alunos") || sql.includes(" from missoes");
}

code.addEventListener("keydown", (event) => {
  if (event.key === "Tab") {
    event.preventDefault();
    const start = code.selectionStart;
    const end = code.selectionEnd;
    code.value = `${code.value.slice(0, start)}    ${code.value.slice(end)}`;
    code.selectionStart = code.selectionEnd = start + 4;
  }
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    event.preventDefault();
    runCode();
  }
});

code.addEventListener("input", () => {
  const beforeCursor = code.value.slice(0, code.selectionStart);
  const match = beforeCursor.match(/[A-Za-z_][A-Za-z_]*$/);
  if (!match) {
    autocomplete.hidden = true;
    return;
  }

  const term = match[0].toLowerCase();
  const currentContext = challenges[currentIndex]?.context || "";
  const activeSuggestions = sqlSuggestions[currentContext] || baseSuggestions;
  const matches = activeSuggestions.filter((item) => item.toLowerCase().startsWith(term)).slice(0, 6);
  if (!matches.length || term.length < 2) {
    autocomplete.hidden = true;
    return;
  }

  autocomplete.innerHTML = matches
    .map((item) => `<button type="button" data-value="${item}">${item}</button>`)
    .join("");
  autocomplete.hidden = false;
});

autocomplete.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;

  const value = button.dataset.value;
  const start = code.selectionStart;
  const before = code.value.slice(0, start);
  const after = code.value.slice(code.selectionEnd);
  const replaced = before.replace(/[A-Za-z_][A-Za-z_]*$/, value);

  code.value = replaced + after;
  code.focus();
  code.selectionStart = code.selectionEnd = replaced.length;
  autocomplete.hidden = true;
});

document.addEventListener("click", (event) => {
  if (!autocomplete.contains(event.target) && event.target !== code) {
    autocomplete.hidden = true;
  }
});

document.querySelector("#runCell").addEventListener("click", runCode);
document.querySelector("#nextChallenge").addEventListener("click", () => {
  if (!solvedChallenges.has(challenges[currentIndex]?.id)) {
    showFeedback(false, "Execute uma resposta correta antes de avançar.");
    return;
  }
  loadChallenge(currentIndex + 1);
});
document.querySelector("#previousChallenge").addEventListener("click", () => loadChallenge(currentIndex - 1));
document.querySelector("#generateChallenges").addEventListener("click", () => {
  generateChallenges({ append: appendMode });
  appendMode = false;
  generateButton.textContent = "Aplicar";
  closeSettings();
});
trackSelect.addEventListener("change", () => {
  appendMode = false;
  generateButton.textContent = "Aplicar";
  generateChallenges();
});
level.addEventListener("change", () => {
  appendMode = false;
  generateButton.textContent = "Aplicar";
  generateChallenges();
});
document.querySelector("#openChallengesFromSettings").addEventListener("click", () => {
  closeSettings();
  openDrawer();
});
document.querySelector("#moreChallenges").addEventListener("click", () => {
  appendMode = true;
  generateButton.textContent = "Adicionar a sessao";
  generateStatus.textContent = "Escolha quantos novos desafios deseja adicionar.";
  openSettings();
  amount.focus();
});
document.querySelector("#closeChallenges").addEventListener("click", closeDrawer);
document.querySelector("#openSettings").addEventListener("click", openSettings);
document.querySelector("#closeSettings").addEventListener("click", closeSettings);
drawer.addEventListener("click", (event) => {
  if (event.target === drawer) closeDrawer();
});
settingsDrawer.addEventListener("click", (event) => {
  if (event.target === settingsDrawer) closeSettings();
});
search.addEventListener("input", renderList);

generateChallenges();
