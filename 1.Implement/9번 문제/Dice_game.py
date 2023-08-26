import sys
sys.stdin = open('input.txt', 'rt')
#1st trial
"""n = int(input())
res = -2147000000
for i in range(n):
    tmp = list(map(int, input().split()))
    money = 0
    if tmp[0] == tmp[1] and tmp[1] == tmp[2] and tmp[0] == tmp[2]:
        money = 10000 + 1000*tmp[0]
    elif tmp[0] == tmp[1] or tmp[0] == tmp[2]:
        money = 1000 + 100*tmp[0]
    elif tmp[1] == tmp[2]:
        money = 1000 + 100*tmp[1]
    else:
        money = max(tmp[0], tmp[1], tmp[2])*100
    if money > res:
        res = money"""

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a*1000
    elif a == b:
        money = 1000 + a*100
    elif b == c:
        money = 1000 + b*100
    else:
        money = c*100
    if money > res:
        res = money


print(res)