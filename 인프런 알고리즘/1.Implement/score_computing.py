import sys
sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
score = 0
add = 1
for x in a:
    if x == 1:
        score += add
        add +=1
    else:
        add = 1
print(score)

