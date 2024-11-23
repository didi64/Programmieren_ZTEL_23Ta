def total(numbers):
    '''returns the sum of numbers
       number list[int|float]
    '''
    tot = 0
    for n in numbers:
        tot = tot + n
    return tot


def bisect(words, subword):
    '''returns the tuples words_with, words_without
       words_with contains all words from words that contain subword
       word: str
       subword: str
    '''
    words_with = ()
    words_without = ()
    for word in words:
        if subword in word:
            words_with += (word,)
        else:
            words_without += (word,)

    return words_with, words_without


def find_first(word, char):
    '''returns the position of the first occurrence of
       the letter char in word.
       returns -1 if char does not occur in word
       word: str
       char: str of length 1
    '''
    i = 0
    for c in word:
        if c == char:
            break
        i = i + 1

    if i == len(word):
        i = -1
    return i


def find_all(word, char):
    '''returns the position of the first occurrence of
       the letter char in word.
       returns -1 if char does not occur in word
       word: str
       char: str of length 1
    '''
    indices = ()
    i = -1
    for c in word:
        i = i + 1
        if c != char:
            continue
        indices = indices + (i,)
    return indices


def remove_chars(word, chars):
    '''remove the characers in chars from word
       and return the resulting word
       word: str
       chars: str
    '''
    clean_word = ''
    for c in word:
        if c in chars:
            continue
        clean_word = clean_word + c
    return clean_word



def make_tuple(n):
    '''returns a tuple (0,...,n-1)
       n: int
    '''
    tp = ()
    i = 0
    for _ in ' ' * n:
        tp = tp + (i,)
        i = i + 1
    return tp


def eval_guess(guess, secret):
    '''returns a tuple (ok, i),
       ok is guess == secret, and i is -1,0 or 1 depending on whether
       guess is too small, correct or too big
       guess: int
       secret: int
    '''
    if guess == secret:
        return (True, 0)
    if guess < secret:
        return (False, -1)
    if guess > secret:
       return (False, 1)


def next_guess(guess, evaluation, lower, upper):
    ''' returns a triple (next_guess, lower, upper)
            so that lower <= secret <= upper
        guess: int
        evaluation: -1 (too small) or 1 (too big)
        lower: int (lower <= secret)
        upper: int (secret <= upper)
    '''
    if evaluation == 1:
        upper = guess - 1
    else:
        lower = guess + 1
    n = (lower + upper) // 2
    return n, lower, upper      


def myrange(*args):
    '''own implementation of the range function
       returns tuple(range(*args))
    '''
    start = 0
    step = 1
    if len(args) == 1:
        stop, = args
    elif len(args) == 2:
        start, stop =  args
    elif len(args) == 3:  
        start, stop, step =  args
    else:
        raise Exception('at most 3 arguments expected')

    items = ()
    sign = (-1)**(step < 0)
    i = start
    while sign*i < sign*stop:
        items = items + (i,)
        i = i + step
    return items