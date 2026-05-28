class pessoa:
    def __init__(self, nome, dt_nascimento):
        self._nome = nome
        self._dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._dt_nascimento

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return 2026 - self._dt_nascimento

individuo = pessoa("Rômulo", 1988)
print(f"Nome: {individuo.nome} \t Idade: {individuo.idade}")
print(f"Nome: {individuo.get_nome()} \t Idade: {individuo.get_idade()}")
