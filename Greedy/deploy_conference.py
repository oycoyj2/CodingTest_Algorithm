import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
seq=[]
for i in range(n):
    s, e = map(int, input().split())
    seq.append((s, e))
seq.sort(key=lambda x: (x[1], x[0]))
last = 0
cnt = 0
for x in seq:
    if x[0] >= last:
        last = x[1]
        cnt += 1
print(cnt)