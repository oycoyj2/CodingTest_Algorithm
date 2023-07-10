def count(dis, a):
    cnt=1
    lately = a[0]
    for x in a:
        if x-lately >= dis:
            lately = x
            cnt+=1
    return cnt

if __name__ == '__main__':
    import sys
    sys.stdin = open("input.txt", 'rt')
    n, c = map(int, input().split())
    a=[]
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    lt = 1
    rt = a[-1]-a[0]
    res=0
    while lt <= rt:
        mid = (lt + rt)//2
        if count(mid, a) >= c:
            res = mid
            lt = mid + 1
        else:
            rt = mid - 1

    print(res)