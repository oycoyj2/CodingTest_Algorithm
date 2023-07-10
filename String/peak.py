import sys
sys.stdin = open('input.txt', 'rt')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

"""for i in range(n):
    a[i].insert(0, 0)
    a[i].append(0)
a.insert(0, [0]*(n+2))
a.append([0]*(n+2))"""

a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(4):
            if a[i+dx[k]][j+dy[k]] >= a[i][j]:
                break
        else:
            cnt += 1
#파이썬처럼
"""if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):"""
print(cnt)