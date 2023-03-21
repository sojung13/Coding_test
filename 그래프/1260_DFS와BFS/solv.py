import sys
sys.stdin = open('input.txt','r')

from collections import deque
# bfs
def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True       
    
# dfs
def dfs(v):
    print(v,end=" ")
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
            visited[i] = True


# 정점의 개수, 간선의 개수, 탐색 시작 번호
n,m,v = map(int,input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(v))

visited = [False] * (n+1)
print(dfs(v))