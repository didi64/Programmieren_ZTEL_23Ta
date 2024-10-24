#! /home/studi/venvs/python3.13/bin/python

'''
allows to live update notebooks
edit_contents -a [-l 02] files
adds the files to contents 02: ...
and pushes the files to notebooks/live_pushes if there are no confilcts

edit_contents -a [-l 02] files
removes the files only from contents 02:

-l/--lesson defaults to 3141
'''

import argparse
import os.path
import subprocess
import sys


REPODIR = '/home/studi/work/.src/'
CONTENTS = REPODIR + 'contents.txt'
PUSHDIRNAME = 'live_pushes'
PUSHDIR = REPODIR + PUSHDIRNAME + '/'
NOTEBOOKS = REPODIR + 'notebooks/'


def get_contents():
    with open(CONTENTS) as f:
        contents = {}
        for line in f:
            line = line.strip()
            idx = line.index(':')
            key = int(line[:idx])
            values = line[idx+1:].strip().split()
            contents[key] = set(values)
        return contents


def write_contents(contents):
    with open(CONTENTS, 'w') as f:
        for k, v in contents.items():
            items = ' '.join(sorted(v))
            line = f'{k}:{items}'
            f.write(line + '\n')


def find_find(name, path, exclude_dirs=()):
    results = []
    for root, dirs, files in os.walk(path):
        if path in exclude_dirs:
            continue
        if name in files:
            results.append(os.path.join(root, name))
    return results


def push_files(files):
    '''add, commit and push files'''
    files = tuple(files)
    pushfiles = tuple(PUSHDIR + file for file in files)
    commit_msg = f'live pushed {pushfiles}'
    cmds = [('cp', '-i') + files + (PUSHDIR,),
            ('git', '-C', REPODIR, 'add') + pushfiles,
            ('git', '-C', REPODIR, 'commit', '-m', commit_msg),
            ('git', '-C', REPODIR, 'push'),
            ]
    for cmd in cmds:
        subprocess.run(cmd)


p = argparse.ArgumentParser()
p.add_argument('-a', '--add', action='store_true')
p.add_argument('-r', '--remove', action='store_true')
p.add_argument('-l', '--lesson', type=int, default=3141)
p.add_argument('files', nargs='+')

args = p.parse_args()
# print(args)

# test if CONTENTS exists
if not os.path.isfile(CONTENTS):
    print(f'No file {CONTENTS} found!')
    sys.exit(1)


# test if files in args.files are files that exist
for file in args.files:
    is_file = os.path.isfile(file)
    # is_dir = os.path.isdir(file)
    if is_file:
        continue
    print(f'No file {file} found!')
    sys.exit(1)


contents = get_contents()
key = args.lesson

if args.add:
    items = contents.setdefault(key, set())
    new_files = set()
    for file in args.files:
        fs = find_find(file, NOTEBOOKS, exclude_dirs=(PUSHDIRNAME,))
        if fs:
            print(f'{file} found {fs}')
            print(f'skipping {file}')
            continue
        items.add(file)
        new_files.add(file)
    push_files(new_files)

elif args.remove:
    if key not in contents:
        print(f'There is not lesson {key}!')
        sys.exit(1)
    contents[key] -= set(args.files)
    if not contents[key]:
        del contents[key]

print(f'{key}: {' '.join(sorted(contents[key]))}')
write_contents(contents)