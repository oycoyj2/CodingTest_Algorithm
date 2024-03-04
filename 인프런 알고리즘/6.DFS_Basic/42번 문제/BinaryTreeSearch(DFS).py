def DFS(v):
    if v > 7:
        return
    else:
        DFS(v * 2)
        DFS(v*2+1)
        print(v, end= "") #함수의 위치가 어디냐에 따라 순회 방식이 달라짐

if __name__ == "__main__":
    DFS(1)