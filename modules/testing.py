'''wants to be able to check only types
   store only value, rest is handled by the checker function
   has a dict checks = {'both, ()
'''

from ansi_color_esc_seqs import fgcolor_ANSIesc as fg_esc
from ansi_color_esc_seqs import bgcolor_ANSIesc as bg_esc
from ansi_color_esc_seqs import reset
from typing import Callable, Iterable
from sys import stderr
import blocktext as BT
import traceback


def _check_both(x, y):
    return x == y and type(x) is type(y)


def _check_value(x, y):
    return x == y


def _check_type(x, y):
    return type(x) is type(y)

def _check_itemtypes(xs, ys):
    return (type(xs) is type(ys) and 
            len(xs) == len(ys) and 
            all(type(x) is type(y) for x, y in zip(xs, ys)))


def _repr_both(x):
    return x 


def _repr_value(x):
    return x 


def _repr_type(x):
    return type(x).__name__


def _repr_itemtypes(xs):
    if not isinstance(xs, Iterable):
        return None
    return type(xs)(type(x).__name__ for x in xs)


def _get_ys(f, argslist):
    ys = []
    for args in argslist:
        args_ = (args,) if type(args) in _basetypes else args
        ys.append(f(*args_))
    return ys


def _validate(f, argslist, reslist, check='both'):
    '''testet, ob f(*args) == result [und ob Typ stimmt]
       fuer alle Paare (args, result) 
       in zip(argslist, reslist)
       returns a report
    '''
    checker, repr_ = _check_checker[check]
    report = {'check': check,
              'ntests': len(argslist),
              }
    
    for i, (args, res) in enumerate(zip(argslist, reslist)):
        args_ = (args,) if type(args) in _basetypes else args
        try:
            got = f(*args_)
        except Exception as e:
            return traceback.print_exception(e, limit=-1)    
        d = {'args': args, 
             'got': repr_(got), 
             'expected': repr_(res),
             }
      
        ok = checker(got, res)
        report[i] = (ok, d)
        
    return report


def _validate_with_fun(f, argslist, f_ref, check='both'):
    checker, repr_ = _check_checker[check]
    report = {'check': check,
              'ntests': len(argslist),
             }
    for i, args in enumerate(argslist):
        args_ = (args,) if type(args) in _basetypes else args
        try:
            got = f(*args_)
        except Exception as e:
            return traceback.print_exception(e, limit=-1)   
      
        res = f_ref(*args_)
        d = {'args': args, 
             'got': repr_(got), 
             'expected': repr_(res),
            }
        
        ok = checker(got, res)
        report[i] = (ok, d)
    return report


def _show_report(report, sep='|', maxlen=50):
    n = report['ntests']
    passed = sum(v[0] for k, v in report.items() if type(k) is int)
   
    if passed > 0:
        print(f'{fg_esc['green']}{passed}/{n} tests passed.{reset}')
        
    if n == passed:
        print(reset)
        return
        
    print(f'{fg_esc['red']}{n-passed}/{n} tests failed.{reset}', file=stderr)
    
    idxs = []
    argss = []
    gots = []
    exps = []
    for k, v in report.items():
        if type(k) is not int or v[0]:
            continue
        idxs.append(str(k+1))
        argss.append(v[1]['args'].__repr__())
        gots.append(v[1]['got'].__repr__())
        exps.append(v[1]['expected'].__repr__())

    colnames = ('test', 'args', 'got', 'expected')
    minwidths = tuple(len(col) for col in colnames)
    maxwidths = (5, 35, 30, 30)
    _widths = tuple(min(maxwidth, max(len(s) for s in ss)) 
                    for maxwidth, ss in zip(maxwidths, (idxs, argss, gots, exps)))
    widths = tuple(max(lower, min(w, upper)) 
                   for w, lower, upper in zip(_widths, minwidths, maxwidths))
             
    fmt = '{{:<{}}}{sep}{{:<{}}}{sep}{{:<{}}}{sep}{{:<{}}}'.format(*widths, sep=sep)
    header = fmt.format(*colnames)

    print(fg_esc['blue_bright'] + header + reset, file=stderr)
    print(fg_esc['blue_bright'] + '-' * len(header) + reset, file=stderr)
    for texts in zip(idxs, argss, gots, exps):
        msg = '\n'.join(BT.texts2lines(texts, widths, sep=sep, maxlen=maxlen))
        print(fg_esc['blue_bright'] + msg + reset, file=stderr)
       
   
def testing(f, xs, f_or_ys, check='both'):
    assert check  in _checks, f'check must be one of {_checks}.'
    assert (isinstance(f, Callable) and isinstance(xs, Iterable)
            and (isinstance(f_or_ys, (Callable, Iterable)))), \
            f'''testing(f: Callable, xs: Iterable, f_or_ys: Callable|Iterable, \
               check: oneOf{_checks}'''
    
    tester = _validate if isinstance(f_or_ys, Iterable) else _validate_with_fun
    report = tester(f, xs, f_or_ys, check)
    if report:
        _show_report(report)



_basetypes = (int, float, str, bool, None, dict, set)
_check_checker = {'both': (_check_both, _repr_both),
           'value': (_check_value, _repr_value),
           'type': (_check_type, _repr_type),
           'itemtypes':  (_check_itemtypes, _repr_itemtypes),
           }
_checks = tuple(_check_checker)