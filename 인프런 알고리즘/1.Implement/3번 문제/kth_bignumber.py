import sys
sys.stdin = open("input.txt", 'rt')

#1st trial
"""N, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
cnt = 0
s = a[0] + a[1] + a[2]
res = 1000000
for i in range(N-2):
    for j in range(i+1, N-1):
        for l in range(j+1, N):
            s = a[i]+a[j]+a[l]
            if s < res:
                res = s
                cnt += 1
            if cnt == k:
                 break
        if cnt == k:
            break
    if cnt == k:
        break
print(res)"""

#revised ans
"""n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(j+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])"""