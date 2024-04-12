import sys
sys.stdin = open('input.txt', 'rt')
from queue import PriorityQueue
n = int(input())
que = PriorityQueue(maxsize=n)

for _ in range(n):
    req = int(input())
    if req == 0:
        if que.empty():
            print('0')
        else:
            tmp = que.get()
            print(str(tmp[1]))
    else:
        que.put((abs(req), req))


