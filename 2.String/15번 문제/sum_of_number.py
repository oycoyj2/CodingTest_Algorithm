import sys
sys.stdin = open("input.txt", 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0]*(n+1)
lt = rt = 0
cnt = 0

for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

while rt < n+1:
    tmp = s[rt] - s[lt]
    if tmp == m:
        cnt += 1
        rt += 1
    elif tmp < m:
        rt += 1
    else:
        lt += 1

print(cnt)