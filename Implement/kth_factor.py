import sys
sys.stdin=open("input.txt", "rt")
#1st trial
"""
n, k = map(int, input().split())
factor = []
for i in range(1,n+1):
    if n % i == 0:
        factor.append(i)
factor.sort()
print(factor[k-1])
"""

#revised ans
"""n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)"""
