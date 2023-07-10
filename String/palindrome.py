import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
for k in range(n):
    a = input()
    word = a.upper()
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" %(i+1))