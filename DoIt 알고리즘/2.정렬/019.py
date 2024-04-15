import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
a = list(map(int, input().split()))

def quickSort(s, e, k):
    global a
    if s < e:
        pivot = partition(s, e)
        if pivot == k:
            return
        elif k < pivot:
            quickSort(s, pivot-1, k)
        else:
            quickSort(pivot+1, e, k)

def swap(i, j):
    global a
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def partition(s, e):
    global a
    if s + 1 == e:  # 두 개의 값을 정렬하는 경우
       if a[s] > a[e]:
           swap(s, e)
       return e

    m = (s+e) // 2
    swap(s, m)
    pivot = a[s]
    i = s+1
    j = e

    while i <= j:
        while pivot < a[j] and j > 0:
            j = j-1
        while pivot > a[i] and i < len(a)-1:
            i = i+1
        if i <= j:
            swap(i, j)
            i = i+1
            j = j-1
    a[s] = a[j]
    a[j] = pivot
    return j

quickSort(0, n-1, k-1)
print(a[k-1])