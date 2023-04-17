import sys
sys.stdin = open('./input.txt','r')
from collections import deque

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    q.append((0,0))
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                
                if arr[nx][ny] == 1:  
                    cnt += 1
                    arr[nx][ny] = 0
                    visited[nx][ny] = True
                    
                elif arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    
    return cnt
time = 0
cheese= []
while True:
    count = bfs()
    cheese.append(count)
    if count == 0:
        break
    time += 1

print(time)
print(cheese[-2])