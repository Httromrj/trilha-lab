class foo:
    # O método __init__ é o construtor da classe.
    # Ele inicializa o objeto com um valor para x.
    # 'x=None' define um valor padrão caso nada seja passado.
    def __init__(self, x = None):
        # 'self._x' é a convenção em Python para indicar que o atributo
        # é "protegido" (interno). Ele armazena o valor real.
        self._x = x

    # @property transforma o método 'x' em um "getter".
    # Isso permite acessar o método como se fosse um atributo (foo.x)
    # em vez de chamar uma função (foo.x()).
    @property
    def x(self):
        # Retorna o valor de _x. Se _x for None, retorna 0.
        return self._x or 0
    
    # @x.setter permite definir o comportamento quando fazemos 'foo.x = valor'.
    @x.setter
    def x(self, value):
        # Neste caso, ele não substitui o valor, ele ACUMULA (soma) ao valor atual.
        # CUIDADO: Se _x for None, '_x += value' causará um TypeError.
        self._x += value

    # @x.deleter define o comportamento quando usamos 'del foo.x'.
    @x.deleter
    def x(self):
        # Em vez de apagar o atributo, define seu valor para -1.
        self._x = -1  

# --- Área de Testes ---

# 1. Instanciação: Cria um objeto da classe foo com self._x = 10
foo = foo(10)

# 2. Acesso (Property Getter): Chama o método @property x
# Imprime: 10
print(foo.x)

# 3. Deleção (Property Deleter): Chama o método @x.deleter
# self._x passa a ser -1
del foo.x

# 4. Acesso: Chama o @property x, que retorna -1
# Imprime: -1
print(foo.x)  

# 5. Atribuição (Property Setter): Chama o método @x.setter (value=10)
# -1 + 10 = 9
# self._x agora é 9
foo.x = 10

# 6. Acesso: Chama o @property x
# Imprime: 9
print(foo.x)
