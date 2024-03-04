import sys
sys.stdin = open("input.txt", 'rt')

def DFS(L, sum):
    global min
    if sum > m:
        return
    if sum == m:
        if L < min:
            min = L
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])


if __name__=="__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    min = 2147000000
    coin.sort(reverse=True)
    DFS(0, 0)
    print(min)