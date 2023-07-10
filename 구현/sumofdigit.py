import sys
sys.stdin = open('input.txt', 'rt')

#1st trial
"""def digit_sum(x):
    while x >  0:
        s = x % 10
        x = x // 10
    return s"""

#2nd
"""
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum"""


n = int(input())
a = list(map(int, input().split()))
max = -2147000000
for x in a:
    tmp = digit_sum(x)
    if tmp > max:
        max = tmp
        res = x

print(res)
