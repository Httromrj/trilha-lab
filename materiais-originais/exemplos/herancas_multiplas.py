import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

class Animais:                
    def __init__(self, nr_patas, **kw): # Adicionado **kw para receber argumentos extras
        super().__init__(**kw)
        self.nr_patas = nr_patas 
        
#Classe __MRO__ serve para mostrar a ordem das Classes.

    def __str__(self):
        # O f-string para listar os atributos corretamente
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}" 
        
class Mamifero(Animais):                
    def __init__(self, pelagem, **kw): 
        super().__init__(**kw) 
        self.pelagem = pelagem 

class Onivoro(Animais):                
    def __init__(self, cor_bico, **kw): 
        super().__init__(**kw) 
        self.cor_bico = cor_bico 

class Canino(Mamifero):                
    def __init__(self, **kw):
        super().__init__(**kw)

#"Ornitorrinco" (início maiúsculo)
class Ornitorrinco(Mamifero, Onivoro):                
    def __init__(self, **kw): 
        super().__init__(**kw) 

# --- Testes ---
# Exemplo Canino
cachorro = Canino(nr_patas=4, pelagem="Tigrado")
print(cachorro)

# Exemplo Ornitorrinco
ornitorrinco = Ornitorrinco(nr_patas=4, pelagem="Marrom", cor_bico="Preto")
print(ornitorrinco)
