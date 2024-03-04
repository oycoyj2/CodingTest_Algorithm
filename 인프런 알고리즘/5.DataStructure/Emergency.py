import sys
from collections import deque
sys.stdin = open("input.txt", 'rt')

n, m = map(int, input().split())
chart = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
chart = deque(chart)
cnt = 0

while True:
    cur = chart.popleft()
    if any(cur[1] < x[1] for x in chart):
        chart.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break


