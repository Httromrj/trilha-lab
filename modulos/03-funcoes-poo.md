# 03 - Funções e POO

## Objetivo

Parar de escrever código solto e começar a criar partes reutilizáveis.

## Funções

Funções recebem entradas, executam uma tarefa e podem devolver uma saída.

```python
def calcular_percentual(parte, total):
    if total == 0:
        return 0
    return parte / total * 100

print(calcular_percentual(25, 100))
```

## Classes

Classes modelam ideias do mundo real.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e tenho {self.idade} anos."
```

## Quando usar POO

Use POO quando você tem objetos com dados e comportamentos relacionados. Evite criar classe só para parecer avançado.

## Desafio rápido

Crie uma classe `Aluno` com:

- nome;
- trilha escolhida;
- pontuação;
- método para adicionar pontos;
- método para exibir o progresso.

