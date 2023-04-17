import sys
sys.stdin = open('input.txt','r')

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        node = q.popleft()
        for i in range(t+1):
            if arr[i][node] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = 1

t = int(input())
n = int(input())
arr = [[0]*(t+1) for _ in range(t+1)]
for i in range(n):
    a,b = map(int,input().split())
    arr[a][b] = arr[b][a] = 1
visited = [0] * (t+1)
bfs(1)
print(sum(visited)-1)