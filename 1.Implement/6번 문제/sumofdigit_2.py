import sys
sys.stdin = open("input.txt", 'rt')

def digit_sum(x):
    sum = 0

    while x != 0:
        sum += x % 10
        x = x // 10

    return sum

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    max = -2147000000
    cnt = 0
    for i in range(n):
        tmp = digit_sum(a[i])
        if tmp > max:
            max = tmp
            res = a[i]

    print(res)