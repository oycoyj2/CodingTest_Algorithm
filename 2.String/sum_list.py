import sys
sys.stdin = open('input.txt', 'rt')
n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while True:
    if p1 == n1 or p2 == n2:
        break
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
#n1이나 n2를 넣지 않아도 끝까지 돈다.
if p1 == n1:
    c = c + b[p2:n2]
else:
    c = c + a[p1:n1]

for i in range(n1+n2):
    print(c[i], end=" ")