'''
ABCDE
BCDE
CDE
DE
E'''
n = 5
for i in range(n):
    for j in range(n - i):
        print(chr(65+j+i), end='')
    print()
