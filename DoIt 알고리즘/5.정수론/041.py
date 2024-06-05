import sys, math
sys.stdin = open('input.txt', 'rt')
n = int(input())
res = n


for i in range(2, int(math.sqrt(n))+1):  #제곱근까지만
    if n % i == 0:                       #i가 소인수인지 확인
        res = res - (res/i)              #결과값 업데이트
        while n % i == 0:                #중복 제거를 방지하기 위해 소인수를 제거
            n /= i

if n > 1:           #제곱근까지 돌기 때문에 소인수가 하나 남는 경우가 있음
    res -= res/n

print(int(res))


