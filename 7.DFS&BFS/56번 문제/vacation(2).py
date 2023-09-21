import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L, sum):
    global res
    if L > n:
        return
    elif L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum)
        DFS(L+a[L][0], sum+a[L][1])

if __name__ == "__main__":
    n = int(input())
    a = []
    res = -2147000000
    for _ in range(n):
        t, p = map(int, input().split())
        a.append((t, p))
    DFS(0, 0)
    print(res)