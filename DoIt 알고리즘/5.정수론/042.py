import sys
sys.stdin = open("input.txt", 'rt')

def DFS(l, s):
    if s == 0:
        return l
    else:
        return DFS(s, l%s)

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    l = max(a, b)
    s = min(a, b)
    ans = a * b / DFS(l, s)
    print(int(ans))
