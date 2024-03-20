import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
score = list(map(int, input().split()))
max_score = 0
avg = 0

for x in score:
    if x > max_score:
        max_score = x

for x in score:
    avg += (x / max_score * 100) / N

print(round(avg, 6))