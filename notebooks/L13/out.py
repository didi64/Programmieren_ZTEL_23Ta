from ipywidgets import Output


def new_out(layout=None):
    '''gibt ein Output-Widget zurueck'''
    if layout is None:
        layout = {'border': '1px solid black'}
    out = Output(layout=layout)
    return out


def print_to_out(out, *args, clear_output=False, **kwargs):
    '''wie print, Ausgabe erfolgt in out'''
    if clear_output:
        out.clear_output()
    with out:
        print(*args, **kwargs)
