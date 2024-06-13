import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')

A, B, C = map(int, input().split())

queue = deque()
queue.append((0, 0))

visited = [[False] * (B+1) for _ in range(A+1)]
visited[0][0] = True

ans = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y))

def BFS():
    while queue:
        x, y = queue.popleft()
        z = C - x - y

        if x == 0:
            ans.append(z)

        # A -> B
        water_quantity = min(x, B-y)
        pour(x-water_quantity, y+water_quantity)

        # A -> C
        water_quantity = min(x, C - z)
        pour(x - water_quantity, y)

        # B -> A
        water_quantity = min(y, A - x)
        pour(x + water_quantity, y - water_quantity)

        # B -> C
        water_quantity = min(y, C - z)
        pour(x, y - water_quantity)

        # C -> A
        water_quantity = min(z, A - x)
        pour(x + water_quantity, y)

        # C -> B
        water_quantity = min(z, B - y)
        pour(x, y + water_quantity)

BFS()

ans.sort()
print(*ans)