import sys
sys.stdin = open("input.txt", 'rt')

n, m = map(int, input().split())
a = [0]*(n+m+2)
cnt = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        a[i+j] += 1
        if cnt < a[i+j]:
            cnt = a[i+j]
for i in range(2, n+m):
    if a[i] == cnt:
        print(i, end=' ')