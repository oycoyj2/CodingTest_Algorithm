import sys
sys.stdin = open('input.txt', 'rt')

a = list(input())
res = 0
cnt = 0
number = []
for x in a:
    if x.isdecimal():
        number.append(x)

for x in number:
    res = res * 10 + int(x)

for i in range(res):
    if res % (i+1) == 0:
        cnt += 1

print(res)
print(cnt)
