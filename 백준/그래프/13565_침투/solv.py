import sys
sys.stdin = open("input.txt", "r")
from collections import deque
# input = sys.stdin.readline()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return visited

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input())))
visited = [[False]*m for _ in range(n)]

for j in range(m):
    if arr[0][j] == 0:
        bfs(0,j)

if True in visited[n-1]:
    print("YES")
else:
    print("NO")
