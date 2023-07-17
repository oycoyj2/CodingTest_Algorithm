import sys
sys.stdin = open('input.txt', 'rt')
#1st tiral
"""a = [0] * 21
for i in range(1, 21):
    a[i] = i
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s)//2+1):
        a[s+i], a[e-i] = a[e-i], a[s+i]

for i in range(1, 21):
    print(a[i], end=" ")"""

#revise ans
a =list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop()

for x in a:
    print(x, end=" ")
