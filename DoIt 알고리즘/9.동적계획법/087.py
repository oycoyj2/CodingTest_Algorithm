import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
D = [0] * 1001
D[0] = D[1] = 1

for i in range(2, N+1):
    D[i] = D[i-1] + D[i-2]

print(D[N] % 10007)