def text2lines(s, width=40, maxlen=None):
    lines = []
    s = s[:maxlen] if maxlen else s
    for line in s.split('\n'):
        idx = 0
        if line == '':
            lines.append(' ' * width)
            continue
        while idx < len(line):
            s = line[idx:idx+width] 
            s += ' ' * (width - len(s))
            idx += width
            lines.append(s)
    return  lines


def merge_blocks(blocks, sep='|'):
    height = max(len(block) for block in blocks)
    for block in blocks:
        m = height - len(block)
        w = len(block[0])
        block.extend([' ' * w] * m)
        
    return [sep.join(lines) for lines in zip(*blocks)]


def texts2lines(texts, widths, sep='|', maxlen=100):
    '''returns a list[str] of table lines
       tests: list[str]
       widths: list[int]
       maxlen: int, tests are truncated to maxlen
    '''
    assert len(texts) == len(widths)
    blocks = [text2lines(s, w, maxlen) for s, w in zip(texts, widths)]
    return merge_blocks(blocks, sep)


def line2block(line, width=40):
    def space():
        return ' ' * bool(line)
        
    lines = []
    parts = line.split()[::-1]
    line = ''
    while parts:
        part = parts.pop()
        if not line and len(part) > width:
            lines.append(part[:width])
            parts.append(part[width:])
        elif len(line) + len(space()) + len(part) > width:
            lines.append(line + ' ' * (width - len(line)))
            line = ''
            parts.append(part)
        elif len(line) + len(space()) + len(part) == width:
            lines.append(line + space() + part)
            line = ''
        else:
            line += space() + part
    if line:
        lines.append(line + ' ' * (width - len(line)))
    return lines