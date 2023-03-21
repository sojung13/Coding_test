import sys
sys.stdin = open('input.txt','r')

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(arr,a,b):
    n = len(arr)
    q = deque()
    q.append((a,b))
    arr[a][b] = 0
    count = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    q.append((nx,ny))
                    count += 1
    return count


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))

cnt = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt.append(bfs(arr,i,j))
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)