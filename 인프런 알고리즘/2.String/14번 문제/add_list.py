import sys
sys.stdin = open('input.txt', 'rt')
n1 = int(input())
a1 = list(map(int, input().split()))
n2 = int(input())
a2 = list(map(int, input().split()))
s = []
p1 = p2 = 0

while (p1 < n1) and (p2 < n2):
    if a1[p1] <= a2[p2]:
        s.append(a1[p1])
        p1 += 1
    else:
        s.append(a2[p2])
        p2 += 1

if p1 == n1:
    s += a2[p2:n2]
else:
    s += a1[p1:n1]

for x in s:
    print(x, end=" ")