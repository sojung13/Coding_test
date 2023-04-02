import sys
sys.stdin = open('./input.txt','r')
from collections import deque
input = sys.stdin.readline

m,n,h = map(int,input().split())
queue = deque()
graph = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        x,y,z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    queue.append((nx,ny,nz))

bfs()
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)