from collections import deque
import sys
sys.stdin = open("input.txt", 'rt')

N = int(input())
A = [[] for i in range(N+1)]
indegree = [0] * (N+1)
selfBuild = [0] * (N+1)

for i in range(1, N+1):
    build = list(map(int, input().split()))
    selfBuild[i] = build[0]
    idx = 1
    while True:
        preTmp = build[idx]
        idx += 1
        if preTmp == -1:
            break
        A[preTmp].append(i)
        indegree[i] += 1


queue = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now]+selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N+1):
    print(result[i] + selfBuild[i])
