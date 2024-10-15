import sys
import os
import subprocess


ROOT = '/home/studi/work'
DATA = '/home/studi/work/.src/data'
SHARE_DIR = '/home/studi/work/share'


def get_prefixes(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    prefixes = []
    for line in lines:
        fname, lname = line.strip().split()
        prefix = fname + '.' + lname
        prefixes.append(prefix)
    return prefixes


def decode(numbers, pin):
    n = 0x10ffff
    data = numbers.split(',')
    s = ''.join([chr((int(x)-pin) % n) for x in data])
    return s


def init_share(user):
    if os.path.exists(SHARE_DIR):
        print('Share Folder already exists!', file=sys.stderr)
        return

    email_prefixes = get_prefixes(DATA + '/klassenliste.txt')
    with open(DATA + '/coordinates.txt') as f:
        coords = f.read()
    tok = decode(coords, 123456)
    # print(tok)
    if tok[-3:] != '95F':
        print('Ungueltiger Pin!', file=sys.stderr)
        return
    if user not in email_prefixes:
        print('Unbekannter Email-Prefix!', file=sys.stderr)
        return
  
    with open(ROOT + '/.user', 'w') as f:
        f.write(user)

    with open(ROOT + '/.token_share', 'w') as f:
        f.write(tok)
        
    print('share folder initialized, cloning repos ...')
    res = subprocess.call(ROOT + '/bin/init_share')
    if res == 0:
        print('Share-Folder fuer User {} eingerichtet.'.format(user))
    else:
        print('Etwas ging schief!  Errorcode {}'.format(res), file=sys.stderr)