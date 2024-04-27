import sys
from collections import deque
sys.stdin = open('input.txt', 'rt')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
board = [[0 for _ in range(M+1)] for _ in range(N+1)]
visited = [[False] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    tmp = str(input())
    for j in range(1, M+1):
        board[i][j] = int(tmp[j-1])

# for i in range(N+1):
#     print(board[i])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 < x <= N and 0 < y <= M:
                if board[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    board[x][y] = board[now[0]][now[1]] + 1
                    queue.append((x, y))

BFS(1, 1)
print(board[N][M])
# for i in range(N+1):
#     print(board[i])