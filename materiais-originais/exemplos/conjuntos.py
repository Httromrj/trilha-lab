import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

#criando SETs - Set elimina valores duplicados em uma lista

print(set([1,2,3,1,3,4]))
print(set("abacaxi"))
print(set(("palio", "gol", "corsa", "marea","gol")))


minha_tupla = ("palio", "gol", "corsa", "marea","gol")
print(set(minha_tupla))

minha_tupla = {"palio", "gol", "corsa", "marea","gol"}
print(minha_tupla)


#CLASSES DO SET

#1 - UNION (Junta dois conjuntos de informações)
conjunto_a = {1,2}
conjunto_b = {4,3}
#conjunto_a.union(conjunto_b)
print(conjunto_a.union(conjunto_b))
#R: {1, 2, 3, 4}

#2 - INTERSECTION (retorna comum aos dois conjuntos)
conjunto_a = {1,2,3,4}
conjunto_b = {4,3,5,6,}
print(conjunto_a.intersection(conjunto_b))
#R: {3, 4}

#3 - DIFFERENCE (retorna os valores diferentes nos dois conjuntos)
conjunto_a = {0,1,2,3,4}
conjunto_b = {4,3,5,6,}
print("Diferença do conjunto A:",conjunto_a.difference(conjunto_b))
print("Diferença do conjunto B:",conjunto_b.difference(conjunto_a))
#R: Diferença do conjunto B: {0, 1, 2} & Diferença do conjunto A: {5, 6}


#4 - SYMMETRIC_DIFFERENCE (retorna os valores diferentes que não estão na intersecção)
conjunto_a = {0,1,2,3,4}
conjunto_b = {4,3,5,6,}
print(conjunto_a.symmetric_difference(conjunto_b))
#R: {0, 1, 2, 5, 6}


#5 - ISSUBSET (Valida os valores pertencem ao conjunto)
conjunto_a = {3,4}
conjunto_b = {4,3,5,6,}
print("Os valores do conjunto B percentem ao conjunto A?",conjunto_a.issubset(conjunto_b))
print("Os valores do conjunto A percentem ao conjunto B?",conjunto_b.issubset(conjunto_a))
#R: True & False


#5 - ISDISJOINT (Conjuntos que não usam intersecção)
conjunto_a = {3,4}
conjunto_b = {4,3,5,6,}
conjunto_c = {1,0}
print("Os valores do conjunto B percentem ao conjunto A?",conjunto_a.isdisjoint(conjunto_b))
print("Os valores do conjunto A percentem ao conjunto C?",conjunto_b.isdisjoint(conjunto_c))
#R: Os valores do conjunto B percentem ao conjunto A? False & Os valores do conjunto A percentem ao conjunto C? True


