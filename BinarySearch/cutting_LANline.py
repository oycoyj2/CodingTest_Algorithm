import sys
sys.stdin = open('input.txt', 'rt')
k, n = map(int, input().split())
LAN = []
for _ in range(k):
    LAN.append(int(input()))
lt = 1
rt = max(LAN)
while lt <= rt:
    tmp = 0
    mid = (lt + rt)//2
    for i in range(k):
        tmp += LAN[i]//mid
    if tmp >= n:
        lt = mid+1
    else:
        rt = mid-1

print(mid)