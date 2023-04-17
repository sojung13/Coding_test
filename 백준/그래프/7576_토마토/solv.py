import sys
sys.stdin = open('./input.txt','r')
from collections import deque

m,n = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
q = deque()

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == -1:
                    continue
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i,j))
bfs()
res = 0
for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)