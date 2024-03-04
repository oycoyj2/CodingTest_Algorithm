import sys
sys.stdin = open("input.txt", 'rt')

n, m = map(int, input().split())
ch=[0]*(n+m+1)
max = -2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
        ch[i+j] += 1
        if ch[i+j] > max:
            max = ch[i+j]

for i in range(1, n+m+1):
    if ch[i] == max:
        print(i, end=' ')