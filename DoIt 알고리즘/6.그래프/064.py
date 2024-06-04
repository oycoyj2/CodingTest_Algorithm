import sys
from queue import PriorityQueue
sys.stdin = open("input.txt", 'rt')
V, E = map(int, input().split())
parent = [0] * (V+1)
pq = PriorityQueue()

for i in range(V+1):
    parent[i] = i
for _ in range(E):
    s, e, w = map(int, input().split())
    pq.put((w, s, e)) #제일 앞 순서를 기준으로 정렬되므로 가중치 변수를 맨앞으로

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

used_edge = 0
res = 0

while used_edge < V-1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        res += w
        used_edge += 1

print(res)




