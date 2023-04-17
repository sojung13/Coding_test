import sys
sys.stdin = open('./input.txt','r')
input = sys.stdin.readline
from collections import deque

a, b = map(int,input().split())
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    arr[i].append(j)
    arr[j].append(i)

def bfs():
    visited = [False for _ in range(n+1)] 
    q = deque()
    q.append((a,0))
    visited[a] = True
    while q:
        now,cnt = q.pop()
        if now == b:
            print(cnt)
            return
        for next in arr[now]:
            if not visited[next]:
                visited[next] = True
                q.appendleft((next,cnt + 1))
    print(-1)

bfs()