import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')
n , l = map(int, input().split())
a = list(map(int, input().split()))
dq = deque()
first_small = 2147000000
second_small = 2147000000

# L번째 까지 로직
for i in range(l):
    dq.append(a[i])
    if a[i] < first_small:
        second_small = first_small
        first_small = a[i]
    elif (a[i] > first_small) and (a[i] < second_small):
        second_small = a[i]
    print(first_small, end=' ')

# L번째 이후 로직
# for i in range(l, n):

print()
print(dq)
