buchstabe_wert = {
 'E': 1,
 'N': 1,
 'S': 1,
 'I': 1,
 'R': 1,
 'T': 1,
 'U': 1,
 'A': 1,
 'D': 1,
 'H': 2,
 'G': 2,
 'L': 2,
 'O': 2,
 'M': 3,
 'B': 3,
 'W': 3,
 'Z': 3,
 'C': 4,
 'F': 4,
 'K': 4,
 'P': 4,
 'Ä': 6,
 'J': 6,
 'Ü': 6,
 'V': 6,
 'Ö': 8,
 'X': 8,
 'Q': 10,
 'Y': 10,
}


def wortwert(wort):
    tot = 0
    for b in wort:
        wert = buchstabe_wert[b.upper()]
        tot += wert
    return tot