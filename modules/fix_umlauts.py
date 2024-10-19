import json
import re
from who_am_i import who_am_i

pat = re.compile('Ae|ae|Oe|oe|Ue|ue')
tt = {'Ae': 'Ä', 'ae': 'ä', 'Oe': 'Ö', 'oe': 'ö', 'Ue': 'Ü', 'ue': 'ü'}


def replace_umlauts(s):
    '''replaces Umlauts in a String using this translation table:
       tt = {'Ae': 'Ä', 'ae': 'ä', 'Oe': 'Ö', 'oe': 'ö', 'Ue': 'Ü', 'ue': 'ü'}
    '''   
    return re.sub(pat, lambda m: tt[m.group(0)], s)


def fix_umlauts():
    '''replaces umlauts in all markdown cells of the current notebook
       using this translation table:
       tt = {'Ae': 'Ä', 'ae': 'ä', 'Oe': 'Ö', 'oe': 'ö', 'Ue': 'Ü', 'ue': 'ü'}
    '''   
    name = who_am_i()['file_name']
    fn = f'{name}.ipynb'
    with open(fn, 'r') as f:
        data = json.load(f)
    for cell in data['cells']:
        if cell['cell_type'] == 'markdown':
            src = cell['source']
            for i, line in enumerate(src):
                src[i] = replace_umlauts(line) 
    with open(fn, 'w') as f:
        json.dump(data, f)