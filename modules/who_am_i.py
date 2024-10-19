import ipynbname


def who_am_i():
    '''returns a dict d with the name and the path of the current notebook, e.g.
       d['file_name'] is 'fix_umlauts'
       d['dir_name']  is '/home/probst/JupyterNotebooks/Prog_ZTel23Ta/notebooks/L02'
    '''
    d = {'file_name': ipynbname.name(),
         'dir_name': ipynbname.path().parent.as_posix(),
         }
    return d