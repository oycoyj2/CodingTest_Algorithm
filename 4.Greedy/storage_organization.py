import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
a = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    a.sort(reverse=True)
    a[0] -= 1
    a[-1] += 1
a.sort(reverse=True)
print(a[0]-a[-1])