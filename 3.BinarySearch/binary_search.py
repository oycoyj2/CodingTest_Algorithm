import sys
sys.stdin = open("input.txt", 'rt')
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = n-1
a.sort()
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] < m:
        lt = mid + 1
    else:
        rt = mid - 1
