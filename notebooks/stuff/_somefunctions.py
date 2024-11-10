
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


_tests = [
    (length, [('',), ('x'), ('01234567',)], [0, 1, 8]),
    (reverse_word, [('abc123',)], ['321cba']),
    (factorial, [(0,), (1,), (10,)], [1, 1, 3628800]),    
    (sum_upto, [(0,), (1,), (10,)], [0, 1, 55]),
    (ox_rect, [(3,)], [None]),
]


if __name__ == '__main__':
    # run tests
    from testing import run_tests
    run_tests(_tests)
