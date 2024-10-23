def reverse_word(word):
    '''returns the reversed word
       word: str
    '''
    drow = ''
    for c in word:
        drow = c + drow
    return drow


def join_words(words):
    '''returns the words as a space-separated string
       words: tuple[str]
    '''
    text = ''
    sep = ' '
    for word in words:
        if text:  # text != ''
            text = text + sep
        text = text + word
    return text