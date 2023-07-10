import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
res=[0]*nc
for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == a[i] and res[j] == 0:
            res[j] = i+1
            break
        if res[j] == 0:
            cnt += 1
print(res)
