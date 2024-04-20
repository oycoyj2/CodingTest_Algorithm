import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
a = [0] * (10001)

for _ in range(n):
    value = int(input())
    a[value] += 1

for i in range(10001):
    if a[i] != 0:
        for _ in range(a[i]):
            print(i)