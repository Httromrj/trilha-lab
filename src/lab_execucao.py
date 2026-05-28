"""Laboratório local para executar pequenos códigos Python pelo navegador.

Este servidor é voltado para estudo local. Ele executa o código digitado pelo
usuário na própria máquina, então não deve ser publicado na internet.
"""

from __future__ import annotations

import ast
import json
import re
import sqlite3
import subprocess
import sys
import tempfile
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from textwrap import dedent


HOST = "127.0.0.1"
PORT = 8850
TIMEOUT_SECONDS = 5
MAX_CODE_SIZE = 20_000
MAX_OUTPUT_SIZE = 12_000
BASE_DIR = Path(__file__).resolve().parents[1]
STATIC_PREFIXES = (
    "assets/",
    "dados/",
    "desafios/",
    "docs/",
    "materiais-originais/",
    "modulos/",
    "projetos/",
    "site/",
    "trilhas/",
)
ALLOWED_IMPORTS = {
    "collections",
    "datetime",
    "json",
    "math",
    "pathlib",
    "pandas",
    "random",
    "re",
    "statistics",
}
BLOCKED_CALLS = {
    "__import__",
    "breakpoint",
    "compile",
    "delattr",
    "dir",
    "eval",
    "exec",
    "exit",
    "getattr",
    "globals",
    "help",
    "locals",
    "open",
    "quit",
    "setattr",
    "vars",
}
BLOCKED_ATTRIBUTES = {
    "chmod",
    "chown",
    "copy",
    "copy2",
    "copyfile",
    "copytree",
    "exec",
    "exec_module",
    "hardlink_to",
    "mkdir",
    "open",
    "popen",
    "read_bytes",
    "read_excel",
    "read_feather",
    "read_html",
    "read_parquet",
    "read_pickle",
    "read_sas",
    "read_spss",
    "read_sql",
    "read_stata",
    "read_table",
    "read_text",
    "remove",
    "rename",
    "replace",
    "rmdir",
    "rmtree",
    "run",
    "spawn",
    "startfile",
    "subprocess",
    "symlink_to",
    "system",
    "to_csv",
    "to_excel",
    "to_feather",
    "to_json",
    "to_parquet",
    "to_pickle",
    "to_sql",
    "unlink",
    "write_bytes",
    "write_text",
}
CONTROLLED_DATA_READS = {"read_csv", "read_json"}
CONTEXT_IMPORTS = {
    "python-base": set(),
    "colecoes": set(),
    "funcoes": set(),
    "pandas": {"pandas"},
}
SQL_BLOCKED_KEYWORDS = re.compile(
    r"\b(insert|update|delete|drop|create|alter|replace|truncate|attach|detach|vacuum|pragma)\b",
    re.IGNORECASE,
)
SQL_CONTEXTS = {
    "sql-base",
    "sql-select-all",
    "sql-select-columns",
    "sql-order-limit",
    "sql-filter",
    "sql-aggregate",
    "sql-join",
}
SQL_ALLOWED_TABLES = {"alunos", "missoes"}
SQL_AGGREGATE_PATTERN = re.compile(r"\b(count|avg|sum|min|max)\s*\(", re.IGNORECASE)


EXAMPLES = {
    "python-base": {
        "title": "Python Base",
        "context": "python-base",
        "code": """nome = "Romulo"
idade = 30
print(f"Olá, {nome}!")
print(f"Daqui a 5 anos você terá {idade + 5} anos.")""",
    },
    "colecoes": {
        "title": "Coleções",
        "context": "colecoes",
        "code": """gastos = [25.90, 12.50, 100.00, 8.75]
limite = 20

print("Total:", sum(gastos))
print("Gastos acima do limite:")

for gasto in gastos:
    if gasto > limite:
        print(gasto)""",
    },
    "funcoes": {
        "title": "Funções",
        "context": "funcoes",
        "code": """def calcular_percentual(parte, total):
    if total == 0:
        return 0
    return parte / total * 100

print(calcular_percentual(35, 100))""",
    },
    "pandas": {
        "title": "Pandas",
        "context": "pandas",
        "code": """import pandas as pd

df = pd.read_csv("dados/relatorio_gorjetas.csv")

print(df.head())
print("Gorjeta média:", df["tip"].mean())""",
    },
}


HTML = r"""<!doctype html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Lab de Execução Python</title>
    <style>
      :root {
        --bg: #071013;
        --panel: #101f21;
        --panel-2: #14282b;
        --text: #f6f7ef;
        --muted: #b9c2bd;
        --green: #6ee7a8;
        --yellow: #ffd166;
        --red: #ff7a70;
        --blue: #66d9ef;
        --line: rgba(255, 255, 255, 0.16);
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      }

      * {
        box-sizing: border-box;
      }

      body {
        margin: 0;
        min-height: 100vh;
        color: var(--text);
        background:
          radial-gradient(circle at 16% 20%, rgba(110, 231, 168, 0.16), transparent 28%),
          radial-gradient(circle at 86% 8%, rgba(102, 217, 239, 0.14), transparent 24%),
          linear-gradient(135deg, #071013 0%, #10211f 48%, #15131f 100%);
      }

      header,
      main {
        width: min(1180px, calc(100% - 32px));
        margin: 0 auto;
      }

      header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        padding: 22px 0;
      }

      a {
        color: var(--green);
      }

      h1,
      p {
        margin-top: 0;
      }

      h1 {
        margin-bottom: 8px;
        font-size: clamp(2rem, 5vw, 4.6rem);
        line-height: 0.95;
        letter-spacing: 0;
      }

      .subtitle {
        max-width: 760px;
        color: var(--muted);
        line-height: 1.6;
      }

      .workspace {
        display: grid;
        grid-template-columns: 240px minmax(0, 1fr);
        gap: 16px;
        padding: 24px 0 40px;
      }

      .panel {
        border: 1px solid var(--line);
        border-radius: 8px;
        background: rgba(16, 31, 33, 0.88);
        overflow: hidden;
      }

      .examples {
        padding: 14px;
      }

      .examples h2,
      .result h2 {
        margin: 0 0 12px;
        font-size: 1rem;
      }

      .example-button,
      .run-button,
      .clear-button {
        width: 100%;
        min-height: 42px;
        margin-bottom: 8px;
        border: 1px solid var(--line);
        border-radius: 8px;
        color: var(--text);
        background: rgba(255, 255, 255, 0.06);
        font: inherit;
        cursor: pointer;
      }

      .example-button:hover,
      .clear-button:hover {
        background: rgba(255, 255, 255, 0.12);
      }

      .editor-shell {
        display: grid;
        grid-template-rows: auto minmax(320px, 1fr) auto minmax(170px, auto);
        min-height: 680px;
      }

      .toolbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        padding: 12px;
        border-bottom: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.05);
      }

      .badge {
        color: var(--yellow);
        font-weight: 800;
      }

      textarea {
        width: 100%;
        min-height: 100%;
        resize: vertical;
        padding: 18px;
        border: 0;
        outline: 0;
        color: var(--text);
        background: #071013;
        font: 500 0.96rem/1.65 "Cascadia Code", Consolas, monospace;
        tab-size: 4;
      }

      .actions {
        display: flex;
        gap: 10px;
        padding: 12px;
        border-top: 1px solid var(--line);
        border-bottom: 1px solid var(--line);
      }

      .run-button {
        width: auto;
        min-width: 150px;
        margin: 0;
        color: #06110d;
        background: var(--green);
        border-color: transparent;
        font-weight: 900;
      }

      .clear-button {
        width: auto;
        min-width: 120px;
        margin: 0;
      }

      .result {
        padding: 14px;
        background: var(--panel-2);
      }

      pre {
        min-height: 120px;
        margin: 0;
        padding: 16px;
        border: 1px solid var(--line);
        border-radius: 8px;
        overflow: auto;
        white-space: pre-wrap;
        color: var(--green);
        background: #061013;
        font: 500 0.92rem/1.6 "Cascadia Code", Consolas, monospace;
      }

      .error {
        color: var(--red);
      }

      .note {
        margin-top: 14px;
        color: var(--muted);
        font-size: 0.92rem;
      }

      @media (max-width: 780px) {
        header {
          align-items: flex-start;
          flex-direction: column;
        }

        .workspace {
          grid-template-columns: 1fr;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <div>
        <h1>Lab de Execução Python</h1>
        <p class="subtitle">
          Teste o código da aula atual e veja a saída na hora.
        </p>
      </div>
      <a href="/site/index.html">Voltar para a trilha</a>
    </header>

    <main class="workspace">
      <aside class="panel examples">
        <h2>Exemplos</h2>
        <button class="example-button" data-example="python-base">Python Base</button>
        <button class="example-button" data-example="colecoes">Coleções</button>
        <button class="example-button" data-example="funcoes">Funções</button>
        <button class="example-button" data-example="pandas">Pandas</button>
        <p class="note">
          Faça pequenas mudanças no exemplo selecionado.
        </p>
      </aside>

      <section class="panel editor-shell">
        <div class="toolbar">
          <strong id="exampleTitle">Python Base</strong>
          <span class="badge" id="contextBadge">contexto: python-base</span>
        </div>
        <textarea id="code" spellcheck="false"></textarea>
        <div class="actions">
          <button class="run-button" id="run">Executar</button>
          <button class="clear-button" id="clear">Limpar saída</button>
        </div>
        <div class="result">
          <h2>Saída</h2>
          <pre id="output">Clique em Executar para ver o resultado.</pre>
        </div>
      </section>
    </main>

    <script>
      const examples = __EXAMPLES__;
      const code = document.querySelector("#code");
      const output = document.querySelector("#output");
      const title = document.querySelector("#exampleTitle");
      const contextBadge = document.querySelector("#contextBadge");

      function loadExample(key) {
        const example = examples[key];
        title.textContent = example.title;
        code.dataset.context = example.context;
        contextBadge.textContent = `contexto: ${example.context}`;
        code.value = example.code;
        output.textContent = "Exemplo carregado. Agora execute ou modifique.";
        output.classList.remove("error");
      }

      async function runCode() {
        output.textContent = "Executando...";
        output.classList.remove("error");

        const response = await fetch("/api/run", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ code: code.value, context: code.dataset.context })
        });

        const result = await response.json();
        output.textContent = result.output || "(sem saída)";

        if (!result.ok) {
          output.classList.add("error");
        }
      }

      document.querySelectorAll("[data-example]").forEach((button) => {
        button.addEventListener("click", () => loadExample(button.dataset.example));
      });

      document.querySelector("#run").addEventListener("click", runCode);
      document.querySelector("#clear").addEventListener("click", () => {
        output.textContent = "";
        output.classList.remove("error");
      });

      code.addEventListener("keydown", (event) => {
        if (event.key === "Tab") {
          event.preventDefault();
          const start = code.selectionStart;
          const end = code.selectionEnd;
          code.value = code.value.slice(0, start) + "    " + code.value.slice(end);
          code.selectionStart = code.selectionEnd = start + 4;
        }

        if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
          event.preventDefault();
          runCode();
        }
      });

      loadExample("python-base");
    </script>
  </body>
</html>
"""


class LabHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/":
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", "/site/index.html")
            self.end_headers()
            return

        if self.path in {"/lab", "/lab/"}:
            self._send_file(BASE_DIR / "site" / "lab.html")
            return

        if self.path == "/api/examples":
            self._send_json(EXAMPLES)
            return

        if self.path.lstrip("/").startswith(STATIC_PREFIXES):
            self._send_static()
            return

        self.send_error(404, "Página não encontrada")

    def do_POST(self) -> None:
        if self.path != "/api/run":
            self.send_error(404, "Endpoint não encontrado")
            return

        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length > MAX_CODE_SIZE:
            self._send_json(
                {"ok": False, "output": "Código muito grande para este laboratório."},
                status=413,
            )
            return

        raw_body = self.rfile.read(content_length)

        try:
            payload = json.loads(raw_body.decode("utf-8"))
        except json.JSONDecodeError:
            self._send_json({"ok": False, "output": "JSON inválido."}, status=400)
            return

        code = str(payload.get("code", ""))
        context = str(payload.get("context", "python-base"))
        stdin_text = str(payload.get("stdin", ""))
        result = run_python(code, context=context, stdin_text=stdin_text)
        self._send_json(result)

    def log_message(self, format: str, *args: object) -> None:
        return

    def _send_html(self) -> None:
        html = HTML.replace("__EXAMPLES__", json.dumps(EXAMPLES, ensure_ascii=False))
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_static(self) -> None:
        relative_path = self.path.lstrip("/")
        target = (BASE_DIR / relative_path).resolve()

        if not str(target).startswith(str(BASE_DIR.resolve())) or not target.is_file():
            self.send_error(404, "Arquivo não encontrado")
            return

        content_type = "text/plain; charset=utf-8"
        if target.suffix == ".html":
            content_type = "text/html; charset=utf-8"
        elif target.suffix == ".css":
            content_type = "text/css; charset=utf-8"
        elif target.suffix == ".js":
            content_type = "text/javascript; charset=utf-8"

        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, target: Path) -> None:
        content_type = "text/plain; charset=utf-8"
        if target.suffix == ".html":
            content_type = "text/html; charset=utf-8"
        elif target.suffix == ".css":
            content_type = "text/css; charset=utf-8"
        elif target.suffix == ".js":
            content_type = "text/javascript; charset=utf-8"
        elif target.suffix == ".json":
            content_type = "application/json; charset=utf-8"

        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, payload: dict[str, object], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run_python(
    code: str, context: str = "python-base", stdin_text: str = ""
) -> dict[str, object]:
    if context in SQL_CONTEXTS:
        return run_sql(code, context=context)

    if context == "ia-base":
        return {
            "ok": True,
            "output": "Resposta registrada para revisão. A próxima etapa será adicionar avaliação por IA/rubrica.",
        }

    if not code.strip():
        return {"ok": False, "output": "Digite algum código antes de executar."}

    safety = validate_code_safety(code, context=context)
    if not safety["ok"]:
        return safety

    script = dedent(code)

    with tempfile.TemporaryDirectory(prefix="jornada_lab_") as temp_dir:
        script_path = Path(temp_dir) / "snippet.py"
        script_path.write_text(script, encoding="utf-8")

        try:
            completed = subprocess.run(
                [sys.executable, "-I", str(script_path)],
                cwd=BASE_DIR,
                text=True,
                capture_output=True,
                input=stdin_text,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return {
                "ok": False,
                "output": f"Tempo limite de {TIMEOUT_SECONDS}s excedido.",
            }

    output = completed.stdout
    if completed.stderr:
        output += ("\n" if output else "") + completed.stderr

    if len(output) > MAX_OUTPUT_SIZE:
        output = output[:MAX_OUTPUT_SIZE] + "\n\n[saída interrompida pelo limite do lab]"

    return {"ok": completed.returncode == 0, "output": output}


def run_sql(code: str, context: str = "sql-base") -> dict[str, object]:
    query = code.strip()
    if not query:
        return {"ok": False, "output": "Digite uma consulta SQL antes de executar."}

    executable = "\n".join(
        line for line in query.splitlines() if not line.strip().startswith("--")
    ).strip()

    if not executable:
        return {"ok": False, "output": "A consulta só tem comentários."}

    executable = executable.rstrip(";").strip()

    if ";" in executable:
        return {
            "ok": False,
            "output": "Execute apenas uma consulta por vez neste lab.",
        }

    first_word = executable.split(None, 1)[0].lower()
    if first_word not in {"select", "with"}:
        return {
            "ok": False,
            "output": "Neste lab SQL, execute apenas consultas SELECT. Comandos de alteração ficam para módulos futuros.",
        }

    if SQL_BLOCKED_KEYWORDS.search(executable):
        return {
            "ok": False,
            "output": "Comando bloqueado. Este lab SQL executa apenas consultas de leitura com SELECT.",
        }

    context_validation = validate_sql_context(executable, context)
    if context_validation:
        return context_validation

    schema_path = BASE_DIR / "trilhas" / "sql" / "dados" / "schema.sql"

    try:
        with sqlite3.connect(":memory:") as connection:
            connection.executescript(schema_path.read_text(encoding="utf-8"))
            cursor = connection.execute(executable)
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description or []]
    except sqlite3.Error as error:
        return {"ok": False, "output": f"Erro SQL: {error}"}

    return {"ok": True, "output": format_sql_result(columns, rows)}


def validate_sql_context(query: str, context: str) -> dict[str, object] | None:
    normalized = " ".join(query.lower().split())

    referenced_tables = re.findall(r"\b(?:from|join)\s+([a-z_][a-z0-9_]*)", normalized)
    invalid_tables = sorted({table for table in referenced_tables if table not in SQL_ALLOWED_TABLES})
    if invalid_tables:
        return {
            "ok": False,
            "output": "Tabela fora do lab: "
            + ", ".join(invalid_tables)
            + ". Use apenas alunos e missoes.",
        }

    if context in {"sql-base", "sql-select-all"}:
        if not re.fullmatch(r"select\s+\*\s+from\s+(alunos|missoes)", normalized):
            return {
                "ok": False,
                "output": "Nesta etapa, use apenas o formato: SELECT * FROM alunos; ou SELECT * FROM missoes;. WHERE, JOIN, ORDER BY e filtros entram depois.",
            }
        return None

    if context == "sql-select-columns":
        blocked = find_sql_keyword(normalized, {"where", "join", "group by", "order by", "limit", "having"})
        if "select *" in normalized or blocked or SQL_AGGREGATE_PATTERN.search(normalized):
            return {
                "ok": False,
                "output": "Nesta etapa, pratique SELECT com nomes de colunas e FROM com uma tabela. Nao use *, filtros, ordenacao, agregacoes ou JOIN.",
            }

    if context == "sql-order-limit":
        blocked = find_sql_keyword(normalized, {"where", "join", "group by", "having"})
        if blocked or SQL_AGGREGATE_PATTERN.search(normalized):
            return {
                "ok": False,
                "output": "Nesta etapa, use apenas ORDER BY ou LIMIT. WHERE, agregacoes e JOIN entram depois.",
            }
        if not find_sql_keyword(normalized, {"order by", "limit"}):
            return {
                "ok": False,
                "output": "Nesta etapa, a consulta precisa usar ORDER BY ou LIMIT.",
            }

    if context == "sql-filter":
        blocked = find_sql_keyword(normalized, {"join", "group by", "having"})
        if blocked or SQL_AGGREGATE_PATTERN.search(normalized):
            return {
                "ok": False,
                "output": "Nesta etapa, use filtros com WHERE em uma tabela. Agregacoes e JOIN entram depois.",
            }
        if not find_sql_keyword(normalized, {"where"}):
            return {
                "ok": False,
                "output": "Nesta etapa, a consulta precisa usar WHERE.",
            }

    if context == "sql-aggregate":
        blocked = find_sql_keyword(normalized, {"join"})
        if blocked:
            return {
                "ok": False,
                "output": "Nesta etapa, pratique agregacoes em uma tabela. JOIN entra na proxima etapa.",
            }
        if not SQL_AGGREGATE_PATTERN.search(normalized):
            return {
                "ok": False,
                "output": "Nesta etapa, a consulta precisa usar COUNT, AVG, SUM, MIN ou MAX.",
            }

    if context == "sql-join":
        if not find_sql_keyword(normalized, {"join", "on"}):
            return {
                "ok": False,
                "output": "Nesta etapa, a consulta precisa usar JOIN com ON.",
            }

    return None


def find_sql_keyword(query: str, keywords: set[str]) -> str | None:
    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword).replace(r"\ ", r"\s+") + r"\b"
        if re.search(pattern, query):
            return keyword
    return None


def format_sql_result(columns: list[str], rows: list[tuple[object, ...]]) -> str:
    if not columns:
        return "Consulta executada sem colunas de resultado."

    rendered_rows = [[format_value(value) for value in row] for row in rows]
    widths = []
    for index, column in enumerate(columns):
        row_widths = [len(row[index]) for row in rendered_rows]
        widths.append(max([len(str(column)), *row_widths]))

    header = " | ".join(str(column).ljust(widths[index]) for index, column in enumerate(columns))
    separator = "-+-".join("-" * width for width in widths)
    body = [
        " | ".join(row[index].ljust(widths[index]) for index in range(len(columns)))
        for row in rendered_rows
    ]

    if not body:
        return f"{header}\n{separator}\n(0 linhas)"

    return "\n".join([header, separator, *body])


def format_value(value: object) -> str:
    if value is None:
        return "NULL"
    return str(value)


def validate_code_safety(code: str, context: str = "python-base") -> dict[str, object]:
    if context not in CONTEXT_IMPORTS:
        return {"ok": False, "output": f"Contexto desconhecido: {context}"}

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        return {"ok": False, "output": format_syntax_error(error)}

    for node in ast.walk(tree):
        blocked_by_context = validate_context_node(node, context)
        if blocked_by_context:
            return blocked_by_context

        if isinstance(node, (ast.Import, ast.ImportFrom)):
            blocked = validate_import(node, context)
            if blocked:
                return blocked

        if isinstance(node, ast.Call):
            blocked = validate_call(node)
            if blocked:
                return blocked

        if isinstance(node, ast.Attribute):
            if node.attr.startswith("__") or node.attr in BLOCKED_ATTRIBUTES:
                return blocked_message(
                    f"Uso de atributo bloqueado: {node.attr}",
                    node.lineno,
                )

        if isinstance(node, ast.Name) and node.id.startswith("__"):
            return blocked_message(f"Nome interno bloqueado: {node.id}", node.lineno)

    return {"ok": True, "output": ""}


def validate_context_node(node: ast.AST, context: str) -> dict[str, object] | None:
    if isinstance(node, (ast.For, ast.While)) and context == "python-base":
        return blocked_message(
            "Laços entram no módulo de coleções e fluxo.",
            node.lineno,
            extra="Neste momento, pratique variáveis, tipos, operadores e strings.",
        )

    if isinstance(node, ast.FunctionDef) and context != "funcoes":
        return blocked_message(
            "Funções entram no módulo de funções.",
            node.lineno,
            extra="Use funções apenas quando estiver no exemplo Funções.",
        )

    if isinstance(node, ast.ClassDef):
        return blocked_message(
            "Classes entram depois, no módulo de POO.",
            node.lineno,
            extra="Neste lab, mantenha o código no tema do exemplo selecionado.",
        )

    return None


def validate_import(
    node: ast.Import | ast.ImportFrom, context: str
) -> dict[str, object] | None:
    if isinstance(node, ast.Import):
        modules = [alias.name for alias in node.names]
    else:
        modules = [node.module or ""]

    for module in modules:
        root = module.split(".", maxsplit=1)[0]
        if root not in ALLOWED_IMPORTS:
            return blocked_message(
                f"Import bloqueado: {module or '(vazio)'}",
                node.lineno,
                extra="Imports liberados: " + ", ".join(sorted(ALLOWED_IMPORTS)),
            )

        context_allowed = CONTEXT_IMPORTS[context]
        if root not in context_allowed:
            allowed_text = ", ".join(sorted(context_allowed)) or "nenhum import"
            return blocked_message(
                f"Import fora do contexto atual: {module}",
                node.lineno,
                extra=f"Neste exemplo, use apenas: {allowed_text}.",
            )

    return None


def validate_call(node: ast.Call) -> dict[str, object] | None:
    name = call_name(node.func)
    if not name:
        return None

    short_name = name.rsplit(".", maxsplit=1)[-1]

    if short_name in BLOCKED_CALLS:
        return blocked_message(f"Função bloqueada: {short_name}", node.lineno)

    if short_name in BLOCKED_ATTRIBUTES:
        return blocked_message(f"Operação bloqueada: {short_name}", node.lineno)

    if short_name in CONTROLLED_DATA_READS:
        blocked = validate_data_read(node, short_name)
        if blocked:
            return blocked

    if "__" in name:
        return blocked_message(f"Acesso interno bloqueado: {name}", node.lineno)

    return None


def validate_data_read(node: ast.Call, function_name: str) -> dict[str, object] | None:
    if not node.args or not isinstance(node.args[0], ast.Constant):
        return blocked_message(
            f"{function_name} precisa receber um caminho literal dentro de dados/",
            node.lineno,
        )

    value = node.args[0].value
    if not isinstance(value, str):
        return blocked_message(
            f"{function_name} precisa receber um caminho de texto.",
            node.lineno,
        )

    normalized = value.replace("\\", "/")
    if (
        "://" in normalized
        or normalized.startswith("/")
        or normalized.startswith("../")
        or not normalized.startswith("dados/")
    ):
        return blocked_message(
            f"{function_name} só pode ler arquivos dentro de dados/",
            node.lineno,
        )

    return None


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        parent = call_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr

    return ""


def blocked_message(
    reason: str,
    line: int,
    extra: str = "Este lab roda em modo seguro para evitar ações perigosas.",
) -> dict[str, object]:
    return {
        "ok": False,
        "output": f"Execução bloqueada na linha {line}.\nMotivo: {reason}\n{extra}",
    }


def format_syntax_error(error: SyntaxError) -> str:
    location = f"linha {error.lineno}" if error.lineno else "linha desconhecida"
    return f"Erro de sintaxe em {location}: {error.msg}"


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), LabHandler)
    print(f"Lab disponível em http://{HOST}:{PORT}")
    print("Pressione Ctrl+C para parar.")
    server.serve_forever()


if __name__ == "__main__":
    main()
