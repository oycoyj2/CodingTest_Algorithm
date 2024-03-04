import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        for i in range(m):
            print(res[i], end=" ")
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res.append(i)
                DFS(L+1)
                ch[i] = 0
                res.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n+1)
    res = []
    cnt = 0
    DFS(0)
    print(cnt)
