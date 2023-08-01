import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
ch = [0]*(n+1)
cnt = 0

for i in range(2, n//2):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n, i):
            ch[j] = 1

for i in range(n//2, n):
    if ch[i] == 0:
        cnt += 1

print(cnt)