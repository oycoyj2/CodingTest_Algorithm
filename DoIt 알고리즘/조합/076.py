import sys
sys.stdin = open('input.txt', "rt")

N, K = map(int, input().split())

combination = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    combination[i][1] = i
    combination[i][i] = 1
    combination[i][0] = 1

for i in range(2, N+1):
    for j in range(1, i):
        combination[i][j] = combination[i-1][j-1] + combination[i-1][j]

print(combination[N][K])
