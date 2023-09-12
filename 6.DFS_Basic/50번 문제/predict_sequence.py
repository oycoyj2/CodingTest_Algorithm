import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L, sum):
    if L == n and sum == f:
        for x in res:
            print(x, end=" ")
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1, sum+res[L]*b[L])
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    ch = [0] * (n+1)
    b = [1] * n
    res = [0] * n
    for i in range(1, n):
        b[i] = b[i-1]*(n-i)//i
    DFS(0, 0)
