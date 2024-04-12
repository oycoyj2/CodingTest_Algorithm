import sys
sys.stdin = open('../1_data_structure/input.txt', 'rt')

n = int(input())
a = []
for _ in range(n):
    tmp = int(input())
    a.append(tmp)

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

for x in a:
    print(x)