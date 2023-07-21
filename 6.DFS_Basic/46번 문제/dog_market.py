import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L, sum):
    global res
    if L == n:
        if sum <= c and sum > res:
            res = sum
    else:
        DFS(L+1, sum+dog[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    c, n = map(int, input().split())
    res=-2147000000
    dog=[]
    for _ in range(n):
        w = int(input())
        dog.append(w)
    DFS(0, 0)
    print(res)