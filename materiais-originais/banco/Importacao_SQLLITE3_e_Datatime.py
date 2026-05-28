import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import sqlite3

conn = sqlite3.connect('dados.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
    )
    ''')
conn.commit()
print("Tabela 'usuarios' criada com sucesso!")
#conn.close()


cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Bob', 25)") 
conn.commit()
print("Usuários adicionados com sucesso!")
#conn.close()   

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()
print("Usuários na tabela:")
for usuario in usuarios:
    print(usuario)
conn.close()    
print("Conexão com o banco de dados fechada.")




#AGENDAMENTO DE TAREFAS - Script para agendar uma tarefa usando o módulo 'datetime' e 'schedule'
import datetime

def executar_relatorio():
    agora = datetime.datetime.now()
    print("Gerando Relatório\n")
    print("Relatório executado em:", agora)

executar_relatorio()    


#CRON JOB - Script para agendar uma tarefa usando o módulo 'schedule' para executar a função 'executar_relatorio' a cada minuto
#Executar um script todos os dias as 8h da manhã:  "08 * * * python3 /caminho/para/seu/script.py"
import datetime
def executar_relatorio():
    vendas = [100, 200, 300]  # Exemplo de dados de vendas
    total_vendas = sum(vendas)
    agora = datetime.datetime.now()
    print("Gerando Relatório de Vendas")
    print("Total de vendas:", total_vendas)
    print("Relatório gerado em:", agora)    

executar_relatorio()
