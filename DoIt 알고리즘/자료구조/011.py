import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
a = [i for i in range(n+1)]
p = 0
res = []
stack = [-1]

for _ in range(n):
    number = int(input())
    if number > a[p]:
        while a[p] < number:
            p += 1
            stack.append(a[p])
            res.append('+')
    if number == stack[-1]:
        stack.pop()
        res.append('-')
    else:
        print("NO")
        break
else:
    for x in res:
        print(x)
