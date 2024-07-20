import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

D = [[0 for i in range(N+1)] for _ in range(2)]

D[0][1] = 0
D[1][1] = 1

for i in range(2, N+1):
    D[0][i] = D[0][i-1] + D[1][i-1]
    D[1][i] = D[0][i-1]

print(D[0][N] + D[1][N])