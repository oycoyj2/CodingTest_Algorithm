import sys
import math
sys.stdin = open('input.txt', 'rt')
a = [0] * (10000001)

for i in range(2, len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a))+1)):
    if a[i] == 0:
        continue
    for j in range(i+i, len(a), i):
        a[j] = 0

def isPalindrome(x):
    a = list(x)
    for i in range(len(a)//2):
        if a[i] != a[-(i+1)]:
            return False
            break
    else:
        return True

n = int(input())

while True:
    if a[n] != 0 and isPalindrome(str(n)):
        print(n)
        break
    n += 1