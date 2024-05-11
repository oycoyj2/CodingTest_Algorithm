import sys
sys.stdin = open("input.txt", 'rt')

m, n = map(int, input().split())
ch = [0] * (n+1)
ch[1] = 1

for i in range(2, n+1):
    for j in range(2*i, n+1, i):
        if ch[j] == 0:
            ch[j] = 1

for i in range(m, n+1):
    if ch[i] == 0:
        print(i)

