import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = -2147000000

for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[i][j]
    if sum > res:
        res = sum

for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j][i]
    if sum > res:
        res = sum

s1 = s2 = 0
for i in range(n):
    s1 += arr[i][i]
    s2 += arr[i][-(i+1)]
if s1 > res:
    res = s1
if s2 > res:
    res = s2

print(res)