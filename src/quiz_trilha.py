"""Quiz simples para abrir a jornada."""

PERGUNTAS = [
    {
        "texto": "Qual função exibe uma mensagem no terminal?",
        "opcoes": ["input", "print", "len"],
        "resposta": "print",
    },
    {
        "texto": "Qual estrutura guarda pares de chave e valor?",
        "opcoes": ["list", "tuple", "dict"],
        "resposta": "dict",
    },
    {
        "texto": "Qual biblioteca é muito usada para DataFrames?",
        "opcoes": ["pandas", "random", "sqlite3"],
        "resposta": "pandas",
    },
]


def perguntar(indice, pergunta):
    print(f"\nMissão {indice}: {pergunta['texto']}")
    for numero, opcao in enumerate(pergunta["opcoes"], start=1):
        print(f"{numero}. {opcao}")

    escolha = input("Escolha uma opção: ").strip()

    try:
        opcao = pergunta["opcoes"][int(escolha) - 1]
    except (ValueError, IndexError):
        print("Entrada inválida. Esta rodada não pontuou.")
        return 0

    if opcao == pergunta["resposta"]:
        print("Resposta certa.")
        return 1

    print(f"Quase. A resposta era: {pergunta['resposta']}")
    return 0


def main():
    print("Jornada Python, IA, Machine Learning e Dados")
    print("Responda ao quiz inicial e descubra seu ponto de partida.")

    pontos = 0
    for indice, pergunta in enumerate(PERGUNTAS, start=1):
        pontos += perguntar(indice, pergunta)

    print(f"\nPontuação final: {pontos}/{len(PERGUNTAS)}")

    if pontos == len(PERGUNTAS):
        print("Você já pode começar pelos desafios do módulo 02.")
    elif pontos >= 1:
        print("Comece pelo módulo 01 e avance praticando.")
    else:
        print("Comece pelo módulo 00 com calma e rode os exemplos.")


if __name__ == "__main__":
    main()

