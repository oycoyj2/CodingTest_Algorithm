import sys
sys.stdin = open('input.txt', 'rt')
a, m = map(int, input().split())
a = list(map(int, str(a)))
n = len(a)
res = []
for i in range(n):
    if res:
        while res[-1] >= a[i]:
            res.pop()
            res.append(a[i])
            m -= 1
    if m == 0 and i == n:
        break
    elif m == 0 and i != n:
        s = i
        for k in range(s, n):
            res.append(a[k])
        break
print(res)
