import sys
sys.stdin = open('./input.txt','r')

n = int(input())
a,b = map(int,input().split())
m = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [False]*(n+1)
result = []

def dfs(v,cnt):
    # 처리해줄 조건
    cnt += 1
    visited[v] = True
    if v == b:
        result.append(cnt)
    # 순환하면서 아직 방문하지 않은 곳이라면 방문 처리해주기
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i,cnt)

dfs(a,0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)