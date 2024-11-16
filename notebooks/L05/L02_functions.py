def count_to(n):
    '''gibt die Zahlen 0,1,...,n-1 aus
       n: int
    '''
    i = 0
    for _ in ' ' * n:
        print(i, end=', ')
        i = i + 1


def length(word):
    '''gibt die Laenge des Worts word zurueck
       word: str
    '''
    i = 0
    for _ in word:
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
    res = 1
    i = 0
    for _ in ' ' * n:
        i = i + 1
        res = res * i
    return res


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