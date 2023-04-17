import sys
sys.stdin = open('input.txt','r')
from collections import deque

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    i,j = map(int,input().split())
    arr[j].append(i)

def bfs(start):
    cnt = 1
    q = deque()
    q.append(start)
    visited = [False for _ in range(n+1)]
    visited[start] = True
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                cnt += 1
                q.append(i)
    return cnt


ans = []
maxCnt = 1
for i in range(1,n+1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)
print(*ans)