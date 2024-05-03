import sys

sys.stdin = open('input.txt', 'rt')

N, M = map(int, input().split())
A = list(map(int, input().split()))
max_num = lt = max(A)
sum_A = rt = sum(A)
res = 0

def takesBlurayCount(size):
    cnt = 1
    saving = 0
    for x in A:
        if (saving + x) > size:
            saving = x
            cnt += 1
        else:
            saving += x
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if takesBlurayCount(mid) <= M:
        rt = mid - 1
    else:
        lt = mid + 1

print(lt)