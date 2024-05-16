import sys
import math
sys.stdin = open('input.txt', 'rt')

a, b = map(int, input().split())
sb = int(math.sqrt(b))
ch = [0] * (sb+1)
cnt = 0

for i in range(2, sb+1):
    ch[i] = i

for i in range(2, int(math.sqrt(sb))+1):
    if ch[i] == 0:
        continue
    for j in range(i+i, sb+1, i):
        ch[j] = 0

for i in range(2, sb+1):
    if ch[i] != 0:
        tmp = ch[i]
        while ch[i] <= b/tmp:
            if ch[i] >= a/tmp:
                cnt += 1
            tmp = tmp * ch[i]

print(cnt)