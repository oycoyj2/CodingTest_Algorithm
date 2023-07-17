import sys
sys.stdin = open("input.txt", 'rt')
s= input()
stack=[]
cnt = 0
for i in range(len(s)):
    if s[i] == ')':
        stack.pop()
        cnt += len(stack)
    else:
        stack.append(s[i])
        cnt += 1
print(cnt)
