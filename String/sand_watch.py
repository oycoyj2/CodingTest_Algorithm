import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

r = int(input())
for i in range(r):
    a, b, c = map(int, input().split())
    if b == 0:
        for j in range(c):
            arr[a-1].append(arr[a-1].pop(0))
    else:
        for j in range(c):
            arr[a-1].insert(0, arr[a-1].pop())
res = 0
for i in range(N):
    if i < N//2:
        for j in range(i, N-i):
            res += arr[i][j]
    else:
        for j in range(N-(i+1), i+1):
            res += arr[i][j]
#원래 방법은 포인터를 통해보는 간접적인 방법이라면 이 방법은 array를 그대로 보는 직접적인 방법이라 할 수 있을 듯
print(res)
