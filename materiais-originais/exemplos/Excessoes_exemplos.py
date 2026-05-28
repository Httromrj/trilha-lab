import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

'''
exception
try
finally
raiserro
'''

#exemplo:
try:
    numero = int("a,b,c")
    numero1 = int("10")
    print(numero)
except ValueError:
    print("Erro de conversão")
finally:
    print("Execução finalizada")



#exemplo:
try:
    numero = 10/0
    print(numero)
except ZeroDivisionError:
    print("Erro: Não possível dividir por zero")


#exemplo:
numero = 10
divisor = 0
resultado = numero / divisor


#exemplo:
def dividir (a,b):
    return a/b
dividir (10,0)


#exemplo:
idade = -5
if idade < 0:
    raise ValueError ("Idade não pode ser negativa")




#TRABALHANDO COM LOG NO PYTHON:
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Mensagem de Debug")
logging.info("Mensagem de info")
logging.warning("Mensagem de warning (Alerta)")
logging.error("Mensagem de erro")



#exemplo:
import logging
logging.basicConfig(level=logging.INFO)  #Nesse trecho o info precisa ser em CAPS 'INFO'
logging.info("Programa iniciado")

'''
#Aqui é um exemplo de como salvar esse log em um arquivo.
import logging

logging.basicConfig(
    filename=r"C:\Users\Romulo\Documents\Cursos\PYTHON\app.log",
    level=logging.INFO
)
logging.info("Sistema iniciado")'''



#PREVENÇÃO DE ERROS - Exemplos:

numero = input("Digite um número: ")
if numero.isdigit():  #verifica se todos os caracteres de uma string são dígitos numéricos.
    numero = int(numero)
    print(numero)
else:
    print("Valor inválido")


#Exemplo:

try:
    numero = int(input("Digite um número: "))
    print(10/numero)
except ZeroDivisionError:
    print("Não é possível dividir por zero.")

except ValueError:
    print("Digite apenas números.")

    
