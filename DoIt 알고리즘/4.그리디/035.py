import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
t = []
cnt = 0
tmp = 0

for _ in range(n):
    s, e = map(int, input().split())
    t.append((s, e))
t.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    if tmp <= t[i][0]:
        tmp = t[i][1]
        cnt += 1

print(cnt)