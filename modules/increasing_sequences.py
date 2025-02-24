def mini_seq(a, n, tot):
    '''returns a sequence s=(a,...) of length n with sum(s) == tot
       and s[:-1] strictly increasing
    '''
    s = tuple(range(a, a+n-1))
    return s + (tot-sum(s),)


def find_index(seq):
    '''it is assumed that seq is strictly increasing with 
       tot := sum(seq) of length n
       if possible,
       returns the largest i so that
       (s_0,...,s_{i-1},s_i + 1) can be extended to a
       strictly increasing sequence with the sum tot and length n
    '''
    margin = 0
    i = len(seq) - 2
    while i >= 0 and margin < 2:
        margin += (seq[i+1]-seq[i]-1)
        i -= 1
    return i+1 if margin > 1 else None


def increase(seq):
    '''if possible,
       returns the next strictly increasing sequence with
       same sum and length
    '''
    if (i := find_index(seq)) is None:
        return

    x = seq[i]+1
    head = seq[:i] + (x,)
    tail = mini_seq(x+1, len(seq)-i-1, sum(seq)-sum(head))
    return head + tail


def is_increasing(seq):
    for i, x in enumerate(seq[:-1]):
        if x >= seq[i+1]:
            return False
    return True


def increasing_seqs(n, tot, start=1):
    '''returns all increasing seqs of length n and sum tot'''
    seq = mini_seq(start, n, tot)
    if not is_increasing(seq):
        return []

    seqs = [seq]
    while seq := increase(seq):
        seqs.append(seq)
    return seqs


def all_increasing_seqs(tot, start=1):
    '''returns all increasing seqs with sum tot'''
    all_seqs = []
    n = 1
    while seqs := increasing_seqs(n, tot, start=start):
        all_seqs += seqs
        n += 1
    return all_seqs
