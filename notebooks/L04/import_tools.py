import sys


def add(path):
    '''fuegt path zur Liste sys.path hinzu
       path: str (Verzeichnis) 
    '''
    if path not in sys.path:
        sys.path = [path] + sys.path
        print(path, ' zu sys.path hinzugefuegt')
    else:
        print(path, ' ist bereits in sys.path')


def remove(path):
    '''loescht path aus der Liste sys.path
       path: str (Verzeichnis) 
    '''
    if path not in sys.path:
        print(path, 'not found in sys.path!')
        return

    syspath = []
    for p in sys.path:
        if p != path:
            syspath = syspath + [p]
    sys.path = syspath
    print(path, 'removed from sys.path!')
