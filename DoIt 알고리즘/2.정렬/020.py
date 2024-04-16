import sys
sys.stdin = open("input.txt", 'rt')

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt+rt)//2
        Dsort(lt, mid)
        Dsort(mid+1, rt)
        p1 = lt
        p2 = mid+1
        tmp = []
        while p1 <= mid and p2 <= rt:
            if a[p1] < a[p2]:
                tmp.append(a[p1])
                p1 += 1
            else:
                tmp.append(a[p2])
                p2 += 1
        if p1 <= mid:
            tmp = tmp+a[p1:mid+1]
        if p2 <= rt:
            tmp = tmp+a[p2:rt+1]
        for i in range(len(tmp)):
            a[lt+i] = tmp[i]

if __name__ == "__main__":
    n = int(input())
    a = [0]*n
    for i in range(n):
        a[i] = int(input())
    Dsort(0, n-1)
    for x in a:
        print(x)
