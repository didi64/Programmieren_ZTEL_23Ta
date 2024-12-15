'''
lang_letterfrequencies: dict
lang_letterfrequencies['de'] and lang_letterfrequencies['en'] are dictionaries.
Each key is a capital letters. The corresponding value is the frequency of that letter.
'''


_lfd_de = {
 'A': 0.06469886702444841,
 'B': 0.01878354203935599,
 'C': 0.030411449016100177,
 'D': 0.05048698071953886,
 'E': 0.17292784734645197,
 'F': 0.016497714172132777,
 'G': 0.029914529914529912,
 'H': 0.047306698469489164,
 'I': 0.07503478433710992,
 'J': 0.0026833631484794278,
 'K': 0.012025442258000396,
 'L': 0.034188034188034185,
 'M': 0.025144106539455372,
 'N': 0.0971973762671437,
 'O': 0.024945338898827267,
 'P': 0.007851321804810176,
 'Q': 0.00019876764062810574,
 'R': 0.069568674219837,
 'S': 0.07841383422778771,
 'T': 0.06112104949314252,
 'U': 0.04323196183661299,
 'V': 0.006658715961041542,
 'W': 0.01878354203935599,
 'X': 0.0002981514609421586,
 'Y': 0.0003975352812562115,
 'Z': 0.011230371695487972,
}

_lfd_en = {
 'A': 0.08165785359344345,
 'B': 0.014937412242703072,
 'C': 0.0278831695197124,
 'D': 0.042820581762415474,
 'E': 0.1294575727700933,
 'F': 0.021908204622631176,
 'G': 0.01991654965693743,
 'H': 0.06074547645365916,
 'I': 0.06970792379928101,
 'J': 0.0014937412242703072,
 'K': 0.00766787161792091,
 'L': 0.03983309931387486,
 'M': 0.023899859588324916,
 'N': 0.06672044135074039,
 'O': 0.07468706121351536,
 'P': 0.01892072217409056,
 'Q': 0.0009460361087045279,
 'R': 0.05974964897081229,
 'S': 0.0627371314193529,
 'T': 0.0906203009390653,
 'U': 0.0278831695197124,
 'V': 0.00975910933189934,
 'W': 0.023899859588324916,
 'X': 0.0014937412242703072,
 'Y': 0.01991654965693743,
 'Z': 0.0007369123373066849,
}

LETTERS = ''.join(_lfd_de)
lang_lfd = {'de': _lfd_de, 
            'en': _lfd_en,
            }


def distance(d1, d2):
    '''returns the Euclidian distance between two dictionaries.
       d1 and d2 are assumed to be frequency dicts, where the
       keys are upper case Letters and the values are floats in [0, 1]
    '''
    residues = ((d1.get(c, 0) - d2.get(c, 0)) ** 2 for c in LETTERS)
    dist = sum(residues) ** 0.5  
    return dist