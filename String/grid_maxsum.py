import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
maxnum = -2147000000
s1=s2=0
for i in range(n):
    if sum(m[i]) > maxnum:
        maxnum = sum(m[i])

for i in range(n):
    s=0
    for j in range(n):
        s += m[j][i]
    if s > maxnum:
        maxnum = s

for i in range(n):
    s1 += m[i][i]
    s2 += m[i][n-(i+1)]
if max(s1, s2) > maxnum:
    maxnum = s1

print(maxnum)