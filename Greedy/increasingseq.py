import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
res=''
tmp=[]
last = 0
lt = 0
rt = n-1

while lt < rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    if len(tmp) == 0:
        break
    else:
        tmp.sort()
        res += tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
        tmp.clear()
print(len(res))
print(res)