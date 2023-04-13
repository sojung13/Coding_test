import sys
sys.stdin = open('./input.txt','r')
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n,m= map(int,input().split())
arr = [[]*(m+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited=[False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i)

cnt = 0
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1
print(cnt)
