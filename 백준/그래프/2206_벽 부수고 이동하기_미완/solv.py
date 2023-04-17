import sys
sys.stdin = open('input.txt','r')
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        # chance = 0
        # if arr[x][y] == 1:
        #     chance += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # chance = 0
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if arr[nx][ny] == 0 and chance <= 1:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = True
                
                # 만약 길을 만난 경우 딱 한 번에 한해서 통과 가능
                if arr[nx][ny] == 1 and chance <= 1:
                    # chance = 0
                    chance += 1
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y] + 1
                    visited[nx][ny] = True

    return arr, chance

n,m = map(int,input().split(" "))
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))
visited = [[False]*m for _ in range(n)]
print(bfs(0,0))