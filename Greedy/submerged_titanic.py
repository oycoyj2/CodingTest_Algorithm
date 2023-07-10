import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
print(a)
lt = 0
rt = n-1
cnt = 0

while True:
    if a[lt]+a[rt] <= m:
        break
    rt -= 1
    cnt += 1

cnt += int(rt/2+0.5)
print(cnt)