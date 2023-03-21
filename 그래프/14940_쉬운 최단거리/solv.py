import sys
sys.stdin = open('./input.txt','r')

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,arr,visited):

    if arr[x][y] == 2 and visited[x][y]==False:
        arr[x][y] = 0
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나지 않고 아직 방문하지 않은 곳일때
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))
                

arr = []
n,m = map(int,input().split(' '))
visited = [[False]*n for _ in range(m)]
for _ in range(n):
    arr.append(list(map(int,input().split(' '))))
for i in range(n):
    for j in range(m):
        if arr[i][j]== 2:
            bfs(i,j,arr,visited)
        if arr[i][j] == 1 and visited[i][j] == False:
            arr[i][j] = -1
        print(arr[i][j], end=" ")
        # print(visited[i][j], end=" ")
    print()
# print(arr)