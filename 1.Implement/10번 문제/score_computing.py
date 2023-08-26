import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = map(int, input().split())
score = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0

print(score)