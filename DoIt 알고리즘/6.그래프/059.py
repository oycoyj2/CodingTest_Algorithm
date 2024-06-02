import sys
sys.stdin = open("input.txt", 'rt')
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1)
distance[1] = 0
for i in range(M):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

for _ in range(N-1):
    for s, e, w in edges:
        if distance[s] != sys.maxsize and distance[s] + w < distance[e]:
            distance[e] = distance[s] + w

m_cycle = False
for s, e, w in edges:
    if distance[s] != sys.maxsize and distance[s] + w < distance[e]:
        m_cycle = True
        break

if not m_cycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)