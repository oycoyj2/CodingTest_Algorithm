import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1][b] = c

for x in matrix:
    for y in x:
        print(y, end=" ")
    print()