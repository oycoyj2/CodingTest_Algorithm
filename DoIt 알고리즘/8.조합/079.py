import sys
sys.stdin = open("input.txt", 'rt')

T = int(input())
D = [[0 for _ in range(30)] for _ in range(30)]

for i in range(30):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i

for i in range(2, 30):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]


for _ in range(T):
    N, M = map(int, input().split())
    print(D[M][N])

