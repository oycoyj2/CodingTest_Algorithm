checkList = [0] * 4
myList = [0] * 4
checkSecret = 0


def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1


def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)

# import sys
# sys.stdin = open("input.txt", 'rt')
#
# def changeACGT(DNA):
#     if DNA == 'A':
#         return 0
#     elif DNA == 'C':
#         return 1
#     elif DNA == 'G':
#         return 2
#     elif DNA == 'T':
#         return 3
#
# def isPassword(origin, check):
#     for i in range(4):
#         if origin[i] > check[i]:
#             return False
#     else:
#         return True
#
# s, p = map(int, input().split())
# a = list(input())
# origin = list(map(int, input().split()))
# check = [0] * 4
# p1 = 0
# p2 = p-1
# for i in range(p):
#     check[changeACGT(a[i])] += 1
# cnt = 0
#
# if isPassword(origin, check):
#     cnt += 1
#
# while p2 < s-1:
#
#     check[changeACGT(a[p1])] -= 1
#     check[changeACGT(a[p2])] -= 1
#     p1 += 1
#     p2 += 1
#     check[changeACGT(a[p1])] += 1
#     check[changeACGT(a[p2])] += 1
#
#     if isPassword(origin, check):
#         cnt += 1
#
# print(cnt)