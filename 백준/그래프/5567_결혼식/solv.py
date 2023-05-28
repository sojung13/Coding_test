import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        cur = q.popleft()
        for i in arr[cur]:
            if not visited[i]:
                visited[i] = visited[cur] + 1
                q.append(i)

bfs(1)
result = 0
for i in range(2,n+1):
    if visited[i] < 4 and visited[i] != 0:
        result += 1
print(result)