import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

#Escrita no arquivo (substituição do texto)
with open("teste.txt", "w") as arquivo:
    arquivo.write("Pyton é uma linguagem poderosa. \n")
    arquivo.write("Estamos aprendendo arquivos.")

#Leitura do arquivo
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)


#Linha por Linha
with open(r"E:\Meus Projetos\Curso Python\teste-.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())


#Adicionar conteúdos no arquivo
with open(r"E:\Meus Projetos\Curso Python\teste-.txt", "a") as arquivo:
    arquivo.write("\nNovo registro adicionado")
#Linha por Linha
with open(r"E:\Meus Projetos\Curso Python\teste-.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# import os

# # Descobre onde o Python está "olhando" neste exato momento
# print("O Python está procurando os arquivos em:", os.getcwd())

 
# # Abrindo e lendo o arquivo de forma segura
# with open("texto.txt", "r", encoding="utf-8") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)


# #Usando uma "raw string" adicionando a letra r antes do caminho:

# with open(r"C:\Users\NomeDoUsuario\Downloads\texto.txt", "r", encoding="utf-8") as arquivo:
#     print(arquivo.read())    
