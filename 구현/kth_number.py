import sys
sys.stdin = open("input.txt", "rt")
#1st trial
"""T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a[s-1:e])
    print("#%d %d" % (i+1, b[k-1]))"""
