import sys
sys.stdin = open("input.txt", 'rt')

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)
for x in a:
    x.insert(0, 0)

S = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    res = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(res)