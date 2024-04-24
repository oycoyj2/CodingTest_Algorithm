import sys
sys.stdin = open("input.txt", 'rt')
N = int(input())

def isPrime(x):
    for i in range(2, int(x/2+1)):
        if x % i == 0:
            return False
    return True

def DFS(x):
    if len(str(x)) == N:
        print(x)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(x * 10 + i):
                DFS(x * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)