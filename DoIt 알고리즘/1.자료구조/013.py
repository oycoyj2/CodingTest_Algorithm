import sys
sys.stdin = open("input.txt", 'rt')
from collections import deque
n = int(input())
dq = deque()
last = 0

for i in range(n):
    dq.append(i+1)

for _ in range(n-1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq)