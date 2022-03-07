import re
from datetime import date, datetime
import datetime






def findStop(text, textA, deli, ignore=0, jump=0, escolha=0): 
    textA = textA.lower()
    deli = deli.lower()
    #print('PRINT TEXTO AQUI: '+ str(text))
    try:
        textA = text.split(textA)
        print('PRINT AQUI1: '+ str(textA))
        textA = textA[1+ignore].split('\n')
        print('PRINT AQUI2: '+ str(textA))
        textA = textA[jump]
        print('PRINT AQUI3: '+ str(textA))

        textA = stopOnNumber(textA)

        
        print('PRINT AQUI4: '+ str(textA))
        textA = textA[escolha]    
        print('PRINT AQUI5: '+ str(textA))
        
        return textA
    except:
        return ''

def stopOnNumber(textA):
    textA = textA.lower()
    for x in range(0,len(textA)):
        var = textA[x]
        if var.isnumeric():
            textA = textA.split(textA[x])
            return textA
        else :
            continue

def stopOnChar(textA):
    textA = textA.lower()
    for x in range(0,len(textA)):
        var = textA[x]
        if var.isalpha():
            textA = textA.split(textA[x])
            return textA
        else :
            continue



# Ajusta o CPF e cnpj
def cpfcnpj(string):
    string = string.replace('.', '').replace('-','').replace('/','')
    if len(string) <14:
        newstring = string[:3] + '.'+string[3:6] + '.'+string[6:9]+ '-'+string[-2:]
    else:
        newstring = string[:2] + '.'+string[2:5] + '.'+string[5:8]+ '/'+string[-6:-2]+'-'+string[-2:]
    print(newstring)

# Remove todo o texto de uma string
def removeText(string, wexcept = 0):
    minus = ''
    if wexcept == 1:
        if '-' in string:
            minus = '-'
    string = re.findall('\d+', string)
    string = ''.join(string)
    string = minus + string
    return(string)

#Soma todos os numeros numa string
def sumAllnumbers(string):
    string = re.findall('\d+', string)
    string = [int(x) for x in string]
    string = sum(string)
    return(string)

# Retorna o dia de hoje
def today():
    return date.today().strftime('%d/%m/%Y')

def modifyDate(ano,mes,dia,q_dias):
    d = date(ano,mes,dia)
    dias = datetime.timedelta(days=q_dias)
    d = d + dias;
    return (d)

def formatDate(data,deli):
    data = data.split(deli)
    print('DATA AQUI: '+str(data))
    if len(data[2]) == 2 :
        formatDate  = data[2]+'/'+data[1]+'/'+data[0]
    else:
        formatDate  = data[0]+'/'+data[1]+'/'+data[2]    
    return formatDate

#Identifica se o textA é um cpf do tipo físico ou Jurídico
def fisicoJuridico(textA):
    if(len(textA)==14):
        return ('Física')
    if(len(textA)==18):
        return ('Jurídica')

def verificaCelouTel(text):
    if text[0] == '(' and text[5] == '9':
        return 'celular'
    elif text[0] != '(' and text[3] == '9':
        return 'celular'
    else:
        return 'telefone'  

#String =  texto de linha retornado
#Deli = delimitador
#Offset = a partir do delimitador quantos números irá para qual lado ?
#Posicao = Qual posição do array criado você quer ?
#Space = Espaço






def replace(variavel, value1, value2):
    replaced = variavel.replace(value1, value2)
    return(replaced)
    
def charSelect(text, textA,split,less=0): 
    textA = textA.lower()
    split = split.lower()
    
    textA = text.split(textA)

    textA = textA[0]
    textA = textA.split(split)
    print(textA)

    length = (len(textA))
    textA = (textA[length - int(less)])
    print(textA)

    return textA  

def capitalizeString(string,split):
    
    string = string.split(split)
    tamanho = len(string)
    print(string)
    print(tamanho)
    y = 0
    element = []
    for y in range(0,tamanho):
        slice = string[y].capitalize()
        element.append(slice)
        nome = ' '.join(element) 
    print(nome)
    return nome    
    
    

        
def findNumber(text):
    string = ""
    for n in text:
        if n.isdigit():
            string = string + n
    print(string)
    return string

#CONVERTE O NOME DO MES PARA NUMERO
#ARG É OPCIONAL CASO TU QUEIRA POR O ZERO NA FRENTE DO MES
#EX: 01    
def convertMonthNameToNumber(string,alg=''):
    string = string.lower()
    if 'janeiro' in string:
        string = string.replace('janeiro',f'{alg}1')
    elif 'fevereiro' in string:
        string = string.replace('feveiro',f'{alg}2')
    elif 'março' in string:
        string = string.replace('março',f'{alg}3')
    elif 'abril' in string:
        string = string.replace('abril',f'{alg}4')
    elif 'maio' in string:
        string = string.replace('maio',f'{alg}5')
    elif 'junho' in string:
        string = string.replace('junho',f'{alg}6')
    elif 'julho' in string:
        string = string.replace('julho',f'{alg}7')
    elif 'agosto' in string:
        string = string.replace('agosto',f'{alg}8')
    elif 'setembro' in string:
        string = string.replace('setembro',f'{alg}9')
    elif 'outubro' in string:
        string = string.replace('outubro','10')
    elif 'novembro' in string:
        string = string.replace('novembro','11')
    else:
        string = string.replace('dezembro','12')
    print(string)
    return string    

