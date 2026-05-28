# 01 - Python Base

## Objetivo

Entender as primeiras peças da linguagem: variáveis, tipos, operadores, entrada, saída e strings.

## Conceitos

- Variável é um nome para guardar um valor.
- Tipo define o que pode ser feito com esse valor.
- `print()` mostra informações.
- `input()` recebe texto do usuário.
- `int()` e `float()` convertem valores numéricos.
- f-string monta textos com variáveis.

## Exemplo

```python
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

ano_nascimento = 2026 - idade

print(f"{nome}, você provavelmente nasceu em {ano_nascimento}.")
```

## Erro comum

`input()` sempre retorna texto. Se você quer fazer conta, precisa converter.

```python
valor = input("Digite um número: ")
print(valor + valor)  # concatena texto

numero = int(valor)
print(numero + numero)  # soma números
```

## Desafio rápido

Crie uma calculadora de metas:

- pergunte o nome da meta;
- pergunte o valor total;
- pergunte quanto a pessoa já juntou;
- mostre quanto falta e o percentual concluído.

