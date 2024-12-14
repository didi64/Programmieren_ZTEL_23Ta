def peek(d, n):
    '''gibt einen dict mit den ersten n (n > 0) 
       oder letzten |n| (n < 0) key-value Paaren zurueck
    '''
    assert type(n) is int and n != 0
    key_iter = d.keys() if n > 0 else reversed(d.keys())
    keys = []
    for i, k in enumerate(key_iter):
        if i == abs(n):
            break
        keys.append(k)
    return {k: d[k] for k in keys}


def sorted_by_key(d, reverse=None):
    return dict(sorted(d.items()), reverse=reverse)


def sorted_by_val(d, reverse=None):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))