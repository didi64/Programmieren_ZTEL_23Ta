def my_insert(i, new, xs):
    '''insert element new at index i into the list xs
       after the insertion, xs[i] == new
    '''
    n = len(xs)
    for i in range(i, n):
        xs[i], new = new, xs[i]
    xs.append(new)

def merge(lefts, rights):
    ''' merge two lists lefts and rights into one,
        preserve the order
    '''
    m, n = len(lefts), len(rights)
    items = []
    i, j = 0, 0
    while i < m and j < n:
        if lefts[i] < rights[j]:
            items.append(lefts[i])
            i += 1
        else:
            items.append(rights[j])
            j += 1
     
    # eine der Listen lefts[i:], rights[j:] ist leer
    items += lefts[i:] + rights[j:] 
    return items


def mergesort(items):
    if len(items) <= 1:
        return items
    i = len(items)//2
    lefts = mergesort_(items[:i])
    rights = mergesort_(items[i:])
    return merge(lefts, rights)


def srange(end, start=0, step=1):
    '''returns ','.join(range(start, end, step))
       without using the function range 
    '''
    i = start
    sign = 1 if step > 0 else -1
    s = ''
    while sign*i < sign*end:
        s = s + str(i) + ','
        i += step
    return s[:-1]