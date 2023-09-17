import sys
sys.stdin = open("input.txt", 'rt')
n = int(input())
for t in range(n):
    tmp = input()
    tmp = tmp.upper()
    for i in range(len(tmp)//2):
        if tmp[i] != tmp[-(i+1)]:
            print("#%d NO" % (t+1))
            break
    else:
        print("#%d YES" % (t+1))
