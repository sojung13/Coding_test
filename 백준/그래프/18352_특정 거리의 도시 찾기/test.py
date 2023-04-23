import sys
sys.stdin = open('input.txt','r')
from collections import deque


def bfs(start):
    q = deque()
    q.append(start) # 일단 1이 들어온다
    ans = []
    while q:
        cur = q.popleft() # 1
        for i in arr[cur]:
            if visited[i] == -1:
                visited[i] = visited[cur] + 1
                q.append(i)
    for i in range(n+1):
        if visited[i] == (distance-1):
            ans.append(i)
            return ans
    return -1

n,m,distance,start = map(int,input().split())
visited = [-1] * (n+1)
arr = [[] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
answer = bfs(start)
for i in answer:
    print(i)