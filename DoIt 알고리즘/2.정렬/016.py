import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
A = list(map(int, input().split()))

not_sorted_arr = {}
for i in range(N):
    not_sorted_arr[A[i]] = i

A.sort()
sorted_arr = {}
for i in range(N):
    sorted_arr[A[i]] = i


res = 0
for i in A:
    res = max(res, not_sorted_arr[i] - sorted_arr[i])

print(res)