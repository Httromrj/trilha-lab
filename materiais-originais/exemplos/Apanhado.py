import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

valor = "10 / 10"
idade = "37"
nome = "Rômulo"
preco_comida = 10

# Usando o f-string do jeito certo: tudo dentro das aspas!
meu_eu = f"Meu nome é: {nome} e minha idade é: {idade}. Pensando em um valor {valor}"
print(meu_eu)

preco = "10.50"
print("O preço do meu teste é: ", float(preco))

# Primeiro transformamos a string em float, e depois em int para arredondar
preco = int(float(preco))
print("Novo preço do meu teste: ", preco)
 
#Preço da comida 
print("Preço da comida: ", float(preco_comida))
print("    ")

#Exemplos de saída de dados:
sobrenome = 'Oliveira'
print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")
print("    ")

#Exemplos de entrada de dados:
nome_usuario = input("Informe o seu nome: ")
print("Olá,",nome_usuario)

#Exemplos de Laços de repetição FOR
texto = input("Informe uma palavra: ")
vogais = "AEIOU"
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print() #Adiciona uma quebra de linha

#Usando FOR para exibir a tabuada de 5, usando função built-in RANGE
                #range(stop) -> range object
                #range(start, stop[, step]) -> range object
                #LIST foi usado para transformar em lista.
for numero in range(0,51,5): #iniciei em 5, exclui o 51 e alternei de 5 em 5.
    print(numero, end=" ")


#Exemplos de Laços de repetição WHILE
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Saque \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Processo de saque iniciado...")
        break
    elif opcao == 2:
        print("Imprimindo Extrato...")  
        break      
    if opcao != 1 or opcao != 2:
        print("Opção não encontrada, digite um número valido")

print("Obrigado") 
        


#Trabalhando com Strings no Python. Vamos aos exemplos
tipo_curso = "PyThon"

print(tipo_curso.upper()) #(O valor da variavel ficou maiúscula)
#Resultado: PYTHON 
print(tipo_curso.lower()) #(O valor da variavel ficou minúscula)
#Resultado: python 
print(tipo_curso.title())  #(O valor da variavel somente com a primeira letra maiúscula)
#Resultado: Python 
print(tipo_curso.lower()) #(O valor da variavel ficou minúscula)
#Resultado: python 

tipo_curso = " PyThon "
print(tipo_curso.strip()) #(O valor da variavel ficou sem espaços em branco da direira e da esquerda)
#Resultado: "PytTon" 
print(tipo_curso.lstrip()) #(Remove os espaços em branco da esquerda)
#Resultado: "PyThon "
print(tipo_curso.rstrip()) #(Remove os espaços em branco da direita)
#Resultado: " PyThon"

tipo_curso = "PyThon"
print(tipo_curso.center(10, "#")) #(Adicona o simbolo de # para preencher a quantidade de caracteres centralizando o valor da variável)
#Resultado: "##PyThon##"
print(".".join(tipo_curso)) #Junta o simbolo de "." ao valor da variável
#Resultado: "P.y.T.h.o.n"



#Interpolação de strings - Vamos ao exemplo
#1 - Usando porcentagem (%s para strings; %d para inteiros; %f para ponto flutuantes)
nome = "Josecleysson"
curso = "Python"
print("Olá, %s . Seja bem vindo(a) ao curso de %s " %(nome,curso))
#Resultado: Olá, Josecleysson . Seja bem vindo(a) ao curso de Python 

#2 - Usando format (Pode ser usado apenas as chaves{} ou usar as {} para selecionar o índice) Não misturar os dois.
nome = "Josecleysson"
curso = "Python"
print("Seja bem vindo(a) ao curso de {1}, senhor(a) {0}. " .format(nome,curso))
#Resultado: Seja bem vindo(a) ao curso de Python, senhor(a) Josecleysson.
print("Seja bem vindo(a) ao curso de {}, senhor(a) {}. " .format(curso,nome))
#Resultado: Seja bem vindo(a) ao curso de Python, senhor(a) Josecleysson. 

#3- Usando o f-string  - Mais utilizada
nome = "Josecleysson"
curso = "Python"
print(f"Seja bem vindo(a) ao curso de {curso}, senhor(a) {nome}.")
#Resultado: Seja bem vindo(a) ao curso de Python, senhor(a) Josecleysson.



#Fatiamento de strings - Ele usa o indice para definir start, stop, step
tipo_curso = "Meu curso de python"
print(tipo_curso[0])
#Resultado: M
print(tipo_curso[:9])
#Resultado: Meu curso
print(tipo_curso[4:11:12])
#Resultado: c
print(tipo_curso[:])
#Resultado: Meu curso de python
print(tipo_curso[::-1])
#Resultado: nohtyp ed osruc ueM


#Strings triplas ou multiplas linhas
curso = "Python"
mensagem = f"""
Esse curso é focado em {curso}.
Ao se inscrever você aprenderá bastante sobre {curso}.
            venha aprender também. """
print(mensagem)

print('''
######################## Menu ########################
      1 - Deposito
      2 - Saque
      3 - Extrato
      0 - Sair
      ''')



