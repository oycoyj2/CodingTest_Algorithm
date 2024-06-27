import sys
sys.stdin = open("input.txt", 'rt')
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
parent = [0]*(n+1)

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(n+1):
    parent[i] = i

for i in range(n):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")