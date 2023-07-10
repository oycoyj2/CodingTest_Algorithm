import sys
sys.stdin = open("input.txt", "rt")

#1st trial
"""n = int(input())
a = list(map(int, input().split()))
dis = 2147000000
mean = int(sum(a)/n + 0.5)
res = (0, 0)
for i in range(n):
    if abs(mean-a[i]) < dis:
        res = (a[i], i)
        dis = abs(mean-a[i])
    if abs(mean-a[i]) == dis:
        if a[i] != res[0]:
            res = (a[i], i)

print(mean, res[1]+1)"""

#revised ans
"""n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/n + 0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)"""