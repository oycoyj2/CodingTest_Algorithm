import sys
sys.stdin = open("input.txt", 'rt')
n = int(input())
player=[]
cnt = n
largest=-2147000000
for _ in range(n):
    h, w = map(int, input().split())
    player.append((h, w))
player.sort(reverse=True)

for x in player:
    if x[1] > largest:
        largest = x[1]
    else:
        cnt -= 1
print(cnt)