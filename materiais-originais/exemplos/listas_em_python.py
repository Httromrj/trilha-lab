import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

carros = ["GOL", "Fox", "Sienna"]
for carro in carros:   #carro foi uma variavel declarada dentro do FOR
    print(carro)

print(carros[0])

print(carros[::])

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")


#exercicio: Pegar todos os numeros pares de uma lista: (1,30,21,2,9,65,34)
numeros = [1,30,21,2,9,65,34] # declaração da lista
pares = [] #uma lista vazia onde vou farmazenar resultados.
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)  #Append é uma forma de adicionar valores a uma lista.

#outra forma abaixo:
#pares = [numero for numero in numeros if numero % 2 == 0]


#MÉTODOS DA CLASSE LIST: 
# 1 - APPEND (Adicionando valores a uma lista)
lista = [] 
lista.append(1)
lista.append("Python")
lista.append([0,30,15,6])

print(lista)
#Resultado: [1, 'Python', [0, 30, 15, 6]]

# 2 - CLEAR (Limpar a lista)
lista = [1, 'Python', [0, 30, 15, 6]]
lista.clear()
#Resultado: Lista vazia


# 3 - COPY (Copia uma lista)
lista = [1, 'Python', [0, 30, 15, 6]]
lista2 = lista.copy()
print(lista2 , lista)


# 4 - COUNT (Conta quantas vezes um objeto aparece na lista)
lista_cores = ["Cinza Vulcan","Branco Perolado","Laranja Amadeirado","Azul"]
print(lista_cores.count("Azul"))


# 5 - EXTEND (Soma valores a uma lista - Cuidado pois ela adiciona valores repetido.)
lista_linguagens = ["Python", "GOLang", "Delphi"]
print(lista_linguagens)
lista_linguagens.extend(["JavaScript", "C ++", "Python"])
print(lista_linguagens)


# 6 - INDEX (Retorna a posição de um objeto - Obs: Se houver valores repetidos só retorna o primeiro)
lista_linguagens = ['Python', 'GOLang', 'Delphi', 'JavaScript', 'C ++', 'Python1']
print(lista_linguagens.index("Python1"))


# 7 -  POP (Entedemos como pilhas - Retorna o ultimo valor da lista)
lista_linguagens = ["Python", "GOLang", "Delphi"]
print(lista_linguagens.pop(0))
print(lista_linguagens.pop())
print(lista_linguagens.pop())
#print(lista_linguagens.pop()) Ao final da lista ele retorna erro caso não encontre nada.


# 8 -  REMOVE (Remove um objeto da lista - OBS: Ele não remove todos objetos repetidos.)
lista_linguagens = ["Python", "GOLang", "Delphi"]
print(lista_linguagens)
lista_linguagens.remove("Delphi")
print(lista_linguagens)


# 9 -  REVERSE (Basicamente o espelhamento da lista - Não altera uma posição com outra)
lista_linguagens = ["Python", "GOLang", "Delphi"]
print(lista_linguagens)
#lista_linguagens[::-1]
lista_linguagens.reverse()
print(lista_linguagens)


# 10 -  SORT (Odernar uma lista)
lista_linguagens = ["Python", "GOLang", "Delphi", "C++", "JAVA"]
print("Lista Principal: ", lista_linguagens)
lista_linguagens.sort() #Ordem alfabetica asc
print(lista_linguagens)
lista_linguagens.sort(reverse= True) #Ordem alfabetica desc
print(lista_linguagens)
lista_linguagens.sort(key=lambda x: len(x)) #Ordem alfabetica das palavras por quantidade de letras asc
print(lista_linguagens)
lista_linguagens.sort(key=lambda x: len(x), reverse= True)#Ordem alfabetica das palavras por quantidade de letras desc
print(lista_linguagens)


# 11 -  LEN (Tamanho da lista ou valores dessa lista)
lista_linguagens = ["Python", "GOLang", "Delphi", "C++", "JAVA"]
print(len(lista_linguagens))


# 12 -  SORTED (função que ordena literaveis)
lista_linguagens = ["Python", "GOLang", "Delphi", "C++", "JAVA"]
print(sorted(lista_linguagens))
print(sorted(lista_linguagens, key=lambda x: len(x))) #Ordem alfabetica das palavras por quantidade de letras asc
print(sorted(lista_linguagens,key=lambda x: len(x), reverse= True))#Ordem alfabetica das palavras por quantidade de letras desc



#List  - Lista (Permite a alteração dos valores da lista)
#Tuple  - Tuplas (Utiliza valores imutáveis em seus vetores e matrizes - SEMPRE TERMINE COM UMA VIRGULA)

Matriz_lista = [ #Usando tuplas)
    [1,"a",2,"b"],
    [3,"c",4,"d"],
    [5,"e",6,"f"]
]

Matriz_tupla = ( #Usando tuplas
    (1,"a",2,"b"),
    (3,"c",4,"d"),
    (5,"e",6,"f"),
)

print(Matriz_tupla [0])
print(Matriz_lista [0][0])
print(Matriz_lista [0][-1])
print(Matriz_lista [-1][-1])


#Outro exemplo usando fatiamento:
tupla = ("p","y","t","h","o","n",)
print(tupla[2:]) # ('t', 'h', 'o', 'n')
print(tupla[:2]) # ('p', 'y')
print(tupla[1:3]) # ('y', 't')
print(tupla[0:4:3]) # ('p', 'h')
print(tupla[::]) # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) # ('n', 'o', 'h', 't', 'y', 'p')

'''''
Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
'''