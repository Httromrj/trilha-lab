import time
import os

#Funções:

def ajuda():                    #Função de Ajuda
    os.system('cls' if  os.name == 'nt' else 'clear')
    print('\033[33m===== Ajuda =====\n')
    print('---Tipos Primitivos:---\033[34m\n'                   #Tipos Primitivos
          '\nint    => Números Inteiros'
          '\nfloat  => Números Reais, com casas decimais'
          '\nbool   => Booleano, Verdadeiro ou Falso'
          '\nstr    => String, textos alfanuméricos\n')

    print('\033[33m--- Operadores Aritiméticos ---\033[34m\n'   #Operadores Aritiméticos
          '\nSoma           => +'
          '\nSubtração      => -'
          '\nMultiplicação  => *'
          '\nDivisão        => /'
          '\nDivisão Inteira=> //'
          '\nMódulo         => %'
          '\nPotência       => **\n')

    print('\033[33m--- Ordem de Precedência ---\033[34m\n'      #Ordem de Precedencia
          '\n1° ()'
          '\n2° **'
          '\n3° * , /, //, %'
          '\n4° +, -\n')

    print('\033[33m--- Manipulação de Texto ---\033[34m\n'      #Manipulação de Texto
          '\n1- A contagem de caracteres começa do 0'
          '\n2- Para selecionar um caractere específico dentro de uma string, usamos []'
          '\n3- Para selecionar uma sequência de caracteres, usamos [:]'
          '\n4- Antes do ":" é o início da seleção e depois do ":" é o fim da seleção'
          '\n5- Usando mais um ":" podemos definir o pulo da seleção, ou seja, os caracteres que serão ignorados'
          '\n6- Por exemplo: [::2] seleciona todos os caracteres pulando de 2 em 2'
          '\n7- Usando len() podemos contar quantos caracteres tem uma string'
          '\n8- Usando .count() podemos contar quantas vezes uma palavra ou caractere aparece em uma string'
          '\n9- Usando .find() podemos encontrar a posição de uma palavra ou caractere em uma string'
          '\n10- Usando .replace() podemos substituir uma palavra ou caractere por outro em uma string'
          '\n11- O .replace() é usado da seguinte forma: .replace("palavra a ser substituída","palavra nova")'
          '\n12- Usando .upper() podemos transformar todos os caracteres em maiúsculo'
          '\n13- Usando .lower() podemos transformar todos os caracteres em minúsculo'
          '\n14- Usando .capitalize() podemos transformar o primeiro caractere em maiúsculo'
          '\n15- Usando .title() podemos transformar o primeiro caractere de cada palavra em maiúsculo'
          '\n16- Usando .strip() podemos remover espaços em branco no início e no fim da string'
          '\n17- Usando .split() podemos dividir uma string em uma lista de palavras'
          '\n18- Usando .join() podemos juntar palavras de uma lista em uma string'
          '\n19- O .join() é usado da seguinte forma: " ".join(lista)\n')

def tipos_primitivos():         #Função Tipos Primitivos
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n1. Vamos começar pelos tipos primitivos !\n\n')

    while True:                 #Questão 1.1
        print('1.1 Para numeros inteiros digitamos:\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'int':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 1.2
        print('1.2 Para números com casas decimais, números reais e etc. digitamos:\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'float':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 1.3
        print('1.3 E para verdadeiro ou falso?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'bool':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 1.4
        print('1.4 Para frases, palavras e afins?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == 'str':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

def operadores_matematicos():   #Função Operadores Aritiméticos
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n2. Operadores matemáticos! Chegou sua hora\n\n')

    while True:                 #Questão 2.1
        print('2.1 Sinal de soma no python:\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '+':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.2
        print('2.2 Sinal para subtração:\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '-':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.3
        print('2.3 E que tal divisão?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '/':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.4
        print('2.4 multiplicação é facil, mas fala ai qual é:\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '*':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.5
        print('2.5 Agora é mais dificil, e Potência ?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '**':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.6
        print('2.6 Divisão Inteira? e ai? lembra?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '//':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:                 #Questão 2.7
        print('2.7 E o resto da divisão?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '%':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

def ordem_de_precedencia():     #Função Ordem de Precedência
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n3. Vamos a ordem de precedêcia !\n\n')
    while True:
        print('3.1 Qual a prioridade 1?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '()':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:
        print('3.2 Qual a ordem de procedência 2 ?\033[33m(Digite "help" para ajuda)')
        resp = input('\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == '**':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:
        print('3.3 Qual a ordem de procedência 3?\033[33m(Digite "help" para ajuda)')
        resp = input('Digite na sequência (multiplicação, Divisão, Divisão Inteira, Resto da Divisão) separando por espaços:\n\033[33mSua Resposta :\033[34m ').lower().strip()
        if resp == ("* / // %"):
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

    while True:
        print('3.4 Por ultimo, ordem de procedência 4?\033[33m(Digite "help" para ajuda)')
        resp = input('Na sequência (soma, subtração) separado por espaços:\n\033[33mSua Resposta :\033[34m ')
        if resp == '+ -':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()
        else:
            print('\033[31mERRADO! Tente de novo!\033[34m')

def manipulacao_texto():        #Função Manipulação de Texto
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n4. Manipulação de Cadeias de Texto! Esse será mais difícil e longo...\n\n')
    frase= '"Estou aprendendo Python"'

    while True:                 #Questão 4.1
        print('4.1 Como selecionar o 2° caractere dentro de uma frase?\033[33m(Digite "help" para ajuda)')
        print('\033[36mfrase = ',frase)
        resp = input('\n\033[33mSua Resposta :\033[34m frase').lower().strip()
        if resp == '[1]':
            print('\033[32mEXATO!\033[34m\n')
            break
        elif resp == 'help':
            ajuda()

... (file truncated)