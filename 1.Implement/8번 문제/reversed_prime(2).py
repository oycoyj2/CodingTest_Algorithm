import sys
sys.stdin = open('input.txt', 'rt')

def reverse(x):
    rev = 0

    while x > 0:
        rev = rev*10 + (x % 10)
        x = x // 10

    return rev

def isPrime(x):
    for i in range(2, x//2+1):
        tmp = x % i
        if tmp == 0:
            return False
            break
    else:
        return True

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        tmp = reverse(a[i])
        if isPrime(tmp):
            print(tmp, end=" ")