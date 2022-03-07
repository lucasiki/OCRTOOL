import re




#Procura a palavra 'textA' dentro do 'text', ignora as 'ignore' ocorrências
#Em seguida, pula as 'jump' linhas e para no delimitador 'deli'
def Exists(text,textA):
    if textA.lower() in text:
        return (textA + ' Encontrado no texto.')
    return ('Texto não encontrado. -> ' + textA)


def find(text, textA, deli, ignore=0, jump=0): 
    textA = textA.lower()
    deli = deli.lower()
    try:
        textA = text.split(textA.lower())

        textA = textA[1+ignore].split('\n')

        textA = textA[jump]
        
        textA = textA.split(deli)
        
        textA = textA[0]    
    
        return repr(textA)
    except:
        return ''

def findSimple(text, textA, deli): 
    textA = textA.lower()
    deli = deli.lower()
    try:
        textA = text.split(textA.lower())
        
        textA = textA[1].split(deli.lower())

        textA = textA[1]    
    
        return textA
    except:
        return ''



#Conta o numero de linhas de 'textA' até 'deli' ignorando as 'ignore' ocorrências
#reduzindo as 'reduce' qtd de linhas
def count(text, textA, deli, ignore=0, reduce=0): 
    textA = textA.lower()
    deli = deli.lower()
    
    textA = text.split(textA)

    textA = textA[1+ignore].split(deli)
    textA = textA[0].split('\n')
    print(len(textA) - reduce)
    return(len(textA)-reduce)
    
