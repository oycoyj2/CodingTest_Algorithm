import sys
sys.stdin = open("input.txt", 'rt')

M = int(input())
N = list(map(int, input().split()))
K = int(input())
sum_N = sum(N)
prob = [1] * M


res = 0

for i in range(M):
    if K <= N[i]:
        for j in range(K):
            prob[i] *= (N[i] - j)/(sum_N - j)
        res += prob[i]

print(res)
