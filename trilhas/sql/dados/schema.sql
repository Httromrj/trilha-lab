CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    cidade TEXT,
    trilha TEXT NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE missoes (
    id INTEGER PRIMARY KEY,
    aluno_id INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    status TEXT NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

INSERT INTO alunos (id, nome, cidade, trilha, pontos) VALUES
(1, 'Ana', 'Sao Paulo', 'Python', 80),
(2, 'Bruno', 'Rio de Janeiro', 'SQL', 55),
(3, 'Carla', 'Salvador', 'Dados', 70);

INSERT INTO missoes (id, aluno_id, titulo, status, pontos) VALUES
(1, 1, 'SELECT basico', 'concluida', 10),
(2, 1, 'Filtros com WHERE', 'pendente', 15),
(3, 2, 'Criar tabela', 'concluida', 10),
(4, 3, 'Agrupar dados', 'pendente', 20);
