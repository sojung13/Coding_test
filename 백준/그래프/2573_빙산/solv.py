import sys
sys.stdin = open('input.txt','r')
from collections import deque

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[x][y] != 0 and arr[nx][ny] == 0:

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(int,input()))
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            bfs(i,j)
