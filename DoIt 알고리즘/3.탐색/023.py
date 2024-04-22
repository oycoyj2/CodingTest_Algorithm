import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", 'rt')

def DFS(v):
    visited[v] = 1
    for i in A[v]:
        if not visited[i]:
            DFS(i)

if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for _ in range(m):
        s, e = map(int, input().split())
        A[s].append(e)      #양방향 에지이므로 양쪽에 에지를 더하기
        A[e].append(s)

    cnt = 0

    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            DFS(i)

    print(cnt)

