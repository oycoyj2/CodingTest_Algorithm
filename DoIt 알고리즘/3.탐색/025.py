import sys

sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())
adList = [[] for i in range(N)]
visited = [0] * (N + 1)
arrive = False

for _ in range(M):
    a, b = map(int, input().split())
    adList[a].append(b)
    adList[b].append(a)


def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in adList[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False


for i in range(N):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
