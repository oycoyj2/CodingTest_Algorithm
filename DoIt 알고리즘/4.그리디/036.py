import sys
sys.stdin = open("input.txt", 'rt')

a = list(map(str, input().split('-')))
res = 0

def mySum(i):
    sum = 0
    tmp = str(i).split('+')
    for x in tmp:
        sum += int(x)
    return sum

for i in range(len(a)):
    tmp = mySum(a[i])
    if i == 0:
        res += tmp
    else:
        res -= tmp

print(res)