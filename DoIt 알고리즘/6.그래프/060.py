import sys
sys.stdin = open('input.txt', 'rt')

N, S, E, M = map(int, input().split())

edge_list = []
for _ in range(M):
    s, e, w = map(int, input().split())
    edge_list.append((s, e, w))

city_money = list(map(int, input().split()))

distance = [-sys.maxsize] * N

distance[S] = city_money[S]

for i in range(N+100):
    for s, e, w in edge_list:
        if distance[s] == -sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e] = sys.maxsize
        elif distance[e] < distance[s] + city_money[e] - w:
            distance[e] = distance[s] + city_money[e] - w
            if i > N-1:
                distance[s] = sys.maxsize

if distance[E] == sys.maxsize:
    print("Gee")
elif distance[E] == -sys.maxsize:
    print("gg")
else:
    print(distance[E])

