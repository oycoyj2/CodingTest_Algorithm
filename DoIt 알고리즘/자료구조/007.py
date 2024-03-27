import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
m = int(input())
a = list(map(int, input().split()))
cnt = 0
a.sort()
p1 = 0
p2 = n-1

while p1 != p2: # 같지 않음으로 하는 것보다 p1 < p2 조건으로 설정하는 것이 바람직하다.
    sum = a[p1] + a[p2]
    if sum == m:
        p2 -= 1
        cnt += 1
    elif sum > m:
        p2 -= 1
    else:
        p1 += 1

print(cnt)