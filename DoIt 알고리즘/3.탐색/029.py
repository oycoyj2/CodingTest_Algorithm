import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    find = False
    target = target_list[i]

    s = 0
    e = len(a)-1
    while s <= e:
        midi = (s+e) // 2
        midv = a[midi]
        if midv > target:
            e = midi - 1
        elif midv < target:
            s = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)