import sys
sys.stdin = open('input.txt', 'rt')
a = [list(map(int, input().split())) for _ in range(7)]
s, e = 0, 4
cnt = 0
for i in range(7):
    for j in range(3):
        for k in range(2):
            if a[i][s+j+k] != a[i][e+j-k]:
                break
        else:
            cnt += 1
        for k in range(2):
            if a[s+j+k][i] != a[e+j-k][i]:
                break
        else:
            cnt += 1
print(cnt)