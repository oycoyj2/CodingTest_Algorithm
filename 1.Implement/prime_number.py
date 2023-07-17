import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
ch = [0] * (n+1)
cnt=0

#1st trial
"""for i in range(2, n//2):
    if ch[i] == 0:
        for j in range(2, n//2):
            if i*j > n:
                break
            ch[i*j] = 1
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1"""

#revised ans
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
