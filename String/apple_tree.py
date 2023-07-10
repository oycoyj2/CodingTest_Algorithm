import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
res = 0

#1st trial
"""for i in range(n):
    if i <= n//2:
        res += sum(grid[i][n//2-i:n//2+(i+1)])
    else:
        res += sum(grid[i][n//2-(n-i-1):n//2+(n-i)])"""

#revised ans
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += grid[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)

