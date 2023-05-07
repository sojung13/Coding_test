import sys
sys.stdin = open('input.txt','r')
from collections import deque

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == -1:
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1
    return arr
    
n = int(input())
r1,c1,r2,c2 = map(int,input().split())
arr = [[-1]*n for _ in range(n)]
bfs(r1,c1)
print(arr[r2][c2])