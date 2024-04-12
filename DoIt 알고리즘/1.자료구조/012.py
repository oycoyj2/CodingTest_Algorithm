import sys

sys.stdin = open("input.txt", 'rt')

N = int(input())
numbers = list(map(int, input().split()))

#시간 초과
"""
for i in range(N):
    oknsu = -1
    for j in range(i + 1, N):
        if numbers[j] > numbers[i]:
            oknsu = numbers[j]
            break
    print(oknsu, end=" ")
"""

#시간 초과
"""
main_stack = sorted(numbers)
sub_stack = []

for x in numbers:
    while sub_stack:
        main_stack.append(sub_stack.pop())
    while True:
        if x == main_stack[-1]:
            if sub_stack:
                print(sub_stack[-1], end=" ")
            else:
                print("-1", end=" ")
            main_stack.pop()
            break
        else:
            sub_stack.append(main_stack.pop())
"""
