from pathlib import Path

a = 1234.26789
b = 'bbb'
c_ = 'ccc'
# print('%04d %d' % (a, a + 1))
# print('{0}aaa'.format(b))
# print(round(2.5))
# print('{0:2.2f} {1:>5.3s} {2:<6.2s}n'.format(a, b, c_))
from common.file_handler import filename_duplicates

# file = './3.6a.txt'
# open(filename_duplicates(file), 'w')
for i in range(10):
    print(i)
    if i == 2:
        i = 6
