import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
cnt = 1
p1, p2 = 1, 1
sum = 1

while p2 != n:
    if sum == n:
        p2 += 1
        sum += p2
        cnt += 1
    elif sum < n:
        p2 += 1
        sum += p2
    else:
        sum -= p1
        p1 += 1

print(cnt)