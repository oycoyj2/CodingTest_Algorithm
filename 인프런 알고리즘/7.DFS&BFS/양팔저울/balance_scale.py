import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L, sum):
    global cnt
    if L == n:
        weight = abs(sum)
        if not ch[weight] == 1:
            ch[weight] = 1
            cnt += 1
    else:
        DFS(L+1, sum-a[L])
        DFS(L+1, sum)
        DFS(L+1, sum+a[L])

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    ch = [0] * (sum(a)+1)
    ch[0] = 1
    cnt = 0
    DFS(0, 0)
    print(sum(a)-cnt)
