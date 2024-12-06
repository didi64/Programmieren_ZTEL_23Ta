def remove_extraspace(s):
    return ' '.join(s.split())


def remove_bracket(s):
    if '(' not in s and ')' not in s:
        return s
    start = s.index('(')
    end = s.index(')', start+1)
    new_s = s[:start] + s[end+1:]
    return remove_extraspace(new_s)


def remove(s, substring):
    if substring not in s:
        return s
    n = len(substring)
    start = s.index(substring)
    new_s = s[:start] + s[start+n:]
    new_s = remove_extraspace(new_s)
    return new_s


def removes(s, substring):
    for ss in substring:
        s = remove(s, ss)
    return s
