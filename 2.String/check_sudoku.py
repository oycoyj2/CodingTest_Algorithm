import sys
sys.stdin = open('input.txt', 'rt')
a = [list(map(int, input().split())) for _ in range(9)]
s = sum(range(1, 10))
check = 0
for i in range(9):
    sum1 = sum2 = 0
    for j in range(9):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if (sum1 != s) and (sum2 != s):
        check += 1
        break

for i in range(3):
    for j in range(3):
        sum = 0
        for m in range(3*i, 3*i+3):
            for n in range(3*j, 3*j+3):
                sum += a[m][n]
        if sum != s:
            check += 1
            break
if check > 0:
    print("NO")
else:
    print("YES")