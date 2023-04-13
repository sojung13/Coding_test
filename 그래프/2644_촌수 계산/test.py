import sys
sys.stdin = open('./input.txt','r')
from collections import deque

n = int(input())
a,b = map(int,input().split())
m = int(input())
arr = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)


def bfs(v,b):
    visited = [False]*(n+1)
    q = deque()
    cnt = 0
    q.append(v)
    while q:
        cur = q.popleft()
        # if cur == b:
        #     cnt += 1
        #     return cnt, visited
        for i in arr[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
            if i == b:
                cnt += 1
                return cnt, visited
    return -1
answer = bfs(a,b)
print(answer)