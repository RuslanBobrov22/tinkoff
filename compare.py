import sys
from main_1 import f


def some_mt(fisrt, second):
    l = len(fisrt) - f(fisrt, second)
    return l / len(fisrt)


st = 0
le = str()
r, w = sys.argv[1:]
pt = open(r).read()
for st in range(0, len(pt.split()), 2):
    st_1 = ''.join(open(pt.split()[st], encoding='utf-8').read().split())
    st_2 = ''.join(open(pt.split()[st + 1], encoding='utf-8').read().split())
    res = some_mt(st_1, st_2)
    le += f'{res} + \n'

with open(w, 'w') as file_end:
    file_end.write(le)
