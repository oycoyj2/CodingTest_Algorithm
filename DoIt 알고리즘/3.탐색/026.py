import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", 'rt')
from collections import deque

def DFS(v):
    visited[v] = 1
    print(v, end=" ")
    for i in A[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = 1
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in A[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)

if __name__ == "__main__":
    n, m, start = map(int, input().split())
    A = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        s, e = map(int, input().split())
        A[s].append(e)
        A[e].append(s)

    for i in range(n+1):
        A[i].sort()

    DFS(start)
    print()
    visited = [0] * (n+1)
    BFS(start)