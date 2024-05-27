import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'rt')

N = int(input())
M = int(input())
myList = [[] for _ in range(N + 1)]
dist = [sys.maxsize] * (N + 1)
visit = [False] * (N + 1)

for _ in range(M):
    S, E, W = map(int, input().split())
    myList[S].append((E, W))

S_idx, E_idx = map(int, input().split())

def dijkstra(S, E):
    pq = PriorityQueue()
    pq.put((0, S))
    dist[S] = 0
    while pq.qsize() > 0:
        nowNode = pq.get()
        now = nowNode[1]
        if not visit[now]:
            visit[now] = True
            for n in myList[now]:
                if not visit[n[0]] and dist[n[0]] > dist[now] + n[1]:
                    dist[n[0]] = dist[now] + n[1]
                    pq.put((dist[n[0]], n[0]))
    return dist[E]

print(dijkstra(S_idx, E_idx))
