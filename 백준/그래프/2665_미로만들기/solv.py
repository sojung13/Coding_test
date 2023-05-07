import sys
sys.stdin = open('input.txt','r')
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[n-1][n-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))
visited = [[-1]*n for _ in range(n)]
print(bfs(0,0))