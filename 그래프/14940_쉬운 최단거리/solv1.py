import sys
sys.stdin = open('./input.txt','r')
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                elif arr[nx][ny] == 0:
                    visited[nx][ny] = 0

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)
    #     print(visited[i][j],end=" ")
    # print()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j],end=" ")
    print()