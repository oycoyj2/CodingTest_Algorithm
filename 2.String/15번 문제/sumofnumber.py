import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
p1, p2 = 0, 1
cnt = 0

while p1 < n:
    tmp = 0
    for i in range(p1, p2):
        tmp += a[i]
    if tmp == m:
        cnt += 1
        p2 += 1
    elif tmp < m:
        p2 += 1
    else:
        p1 += 1

print(cnt)


