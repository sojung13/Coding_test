import sys
sys.stdin = open('input.txt','r')
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    res = 1
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and arr[nx][ny] == 0:
                    res += 1
                    arr[nx][ny] = 1
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return res

n,m,k = map(int,input().split())
arr = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for _ in range(k):
    y1,x1,y2,x2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            arr[i][j] = 1

li = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            arr[i][j] = 1
            answer = bfs(i,j)
            li.append(answer)
print(len(li))
print(*sorted(li))