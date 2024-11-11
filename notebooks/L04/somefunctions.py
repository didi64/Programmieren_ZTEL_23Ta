
def length(s):
    '''gibt die Laenge des Wortes s zurueck
       s: str
    '''
    i = 0
    for _ in s:
        i = i + 1
    return i


def reverse_word(word):
    '''returns the reversed word
       word: str
    '''
    drow = ''
    for c in word:
        drow = c + drow
    return drow


def factorial(n):
    '''returns n!
       n: int
    '''   
    resultat = 1
    i = 0
    for _ in ' ' * n:
        i = i + 1
        resultat = resultat * i
    return resultat


def sum_upto(n):
    '''returns 0+1+...+n
       n: int
    '''
    tot = 0
    i = 0
    for _ in ' ' * n:
        i = i + 1
        tot = tot + i
    return tot


def ox_rect(n):
    '''prints a n x n+1 rectangle wuth Os and Xs 
       n: int
    '''
    i = 0
    for _ in ' ' * n:
        i = i + 1
        os = 'O' * i
        xs = 'X' * (n + 1 - i)
        line = os + xs
        print(line)