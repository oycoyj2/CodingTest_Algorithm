import sys
sys.stdin = open("input.txt", 'rt')
n = int(input())
a=list(map(int, input().split()))
avg=int(sum(a)/n + 0.5)

min_value = 214700000

t=list()
for idx, x in enumerate(a):
    t.append((idx+1, x))
t.sort(key=lambda x: (x[1], -x[0]))

for x in t:
    tmp = abs(x[1]-avg)
    if tmp <= min_value:
        min_value = tmp
        res = x[0]
print(avg, res)