import sys
sys.stdin = open("input.txt", 'rt')

n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0
for i in range(n):   # 음의 정수가 있는 경우라면 첫 번째 값도 다른 두 수의 합이 될 수 있다.
    p1 = 0
    p2 = n-1
    while p1 < p2:
        sum = a[p1] + a[p2]
        if sum == a[i]:
            if p1 != i and p2 != i:
                cnt += 1
                break
            elif p1 == i:
                p1 += 1
            elif p2 == i:
                p2 -= 1
        elif sum > a[i]:
            p2 -= 1
        else:
            p1 += 1
print(cnt)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# cnt = 0
# for i in range(2, n):
#     p1 = 0
#     p2 = n-1
#     while p1 < p2:
#         sum = a[p1] + a[p2]
#         if sum == a[i]:
#             if p1 != i and p2 != i:
#                 cnt += 1
#                 break
#             elif p1 == i:
#                 p1 += 1
#             elif p2 == i:
#                 p2 -= 1
#         elif sum > a[i]:
#             p2 -= 1
#         else:
#             p1 += 1
# print(cnt)
