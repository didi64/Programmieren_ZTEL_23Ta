def validate(f, io_pairs):
    '''testet, ob f(*args) == result
       fuer alle Paare (args, result) 
       in der Liste io_pairs
    '''
    failures = []
    for i, (args, result) in enumerate(io_pairs):
        got = f(*args)
        if got != result:
            failures.append((i, args, got, result))

    n = len(failures)
    m = len(io_pairs)
    if n == 0:
        print('all tests passed')
    else:
        print('{}/{} tests failed'.format(n, m))
        for (i, args, got, expected) in failures:
            fmsg = 'test {}: args: {} got: {} expected: {}'
            print(fmsg.format(i, args, got, expected))
