import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", 'rt')
K = int(input())
IsEven = True

def DFS(N):
    global IsEven
    visited[N] = True
    for i in A[N]:
        if not visited[i]:
            check[i] = (check[N]+1)%2
            DFS(i)
        elif check[N] == check[i]:
            IsEven = False

for _ in range(K):
    V, E = map(int, input().split())
    A = [[] for i in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    IsEven = True

    for i in range(E):
        S, E = map(int, input().split())
        A[S].append(E)
        A[E].append(S)

    for i in range(1, V+1):
        if IsEven:
            DFS(i)
        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")
