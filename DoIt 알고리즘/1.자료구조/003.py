import sys
sys.stdin = open("input.txt", 'rt')

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# for _ in range(m):
#     sum = 0
#     s, e = map(int, input().split())
#     for i in range(s-1, e):
#         sum += a[i]
#     print(sum)

n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = [0]
tmp = 0
for x in a:
    tmp += x
    sum.append(tmp)   # 합 배열 만들기

for _ in range(m):
    s, e = map(int, input().split())
    res = sum[e] - sum[s-1] # 합 배열에서 구간 합 구하기
    print(res)

