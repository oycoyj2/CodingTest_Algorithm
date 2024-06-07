import sys
sys.stdin = open("input.txt", 'rt')

n, k = map(int, input().split())
a = [0] * n
cnt = 0


for i in range(n):
    a[i] = int(input())

for i in range(n-1, -1, -1):
    if a[i] <= k:
        cnt += k // a[i]
        k = k % a[i]

    if k == 0:
        print(cnt)
        break

