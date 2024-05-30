import sys
sys.stdin = open("input.txt", 'rt')

N, M = map(int, input().split())
arr = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    arr[i][i] = 0

for _ in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1


for k in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            arr[s][e] = min(arr[s][e], arr[s][k]+arr[k][e])

min = sys.maxsize

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        tmp += arr[i][j]
    if min > tmp:
        min = tmp
        res = i

print(res)