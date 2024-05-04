import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())
positive_box = []
negative_box = []
zero_chance = 1
just_one = 0
res = 0

for _ in range(N):
    val = int(input())
    if val < 0:
        negative_box.append(val)
    elif val == 0:
        zero_chance = 0
    elif val == 1:
        just_one += 1
    else:
        positive_box.append(val)

positive_box.sort()
negative_box.sort(reverse=True)

while positive_box:
    tmp = 1
    tmp *= positive_box.pop()
    if positive_box:
        tmp *= positive_box.pop()
    res += tmp

while negative_box:
    tmp = 1
    tmp *= negative_box.pop()
    if negative_box:
        tmp *= negative_box.pop()
    else:
        tmp *= zero_chance
    res += tmp

res += just_one

print(res)