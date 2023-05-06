import sys
sys.stdin = open('input.txt','r')
from collections import deque


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    result = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and arr[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    result += 1
    return result

n,m,k = map(int,input().split())
arr = [[0]*m for _ in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
visited = [[False]*m for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            answer = bfs(i,j)
            ans = max(answer,ans)
print(ans)