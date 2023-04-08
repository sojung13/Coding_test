import sys
sys.stdin = open('./input.txt','r')
from collections import deque

n,m = map(int,input().split())
hx,hy = map(int,input().split())
ex, ey = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = [[False]*(m) for _ in range(n)]
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        if x == (ex-1) and y == (ey-1):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 and not visited[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx,ny))
                visited[nx][ny] = True
    return arr[ex-1][ey-1]

# answer = bfs(0,0)
ans = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] == 0
            ans.append(bfs(hx-1,hy-1))
print(ans)