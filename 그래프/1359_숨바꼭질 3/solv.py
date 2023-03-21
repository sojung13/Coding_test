import sys
sys.stdin = open('input.txt','r')
from collections import deque

n,k = map(int,input().split())
visited = [-1 for _ in range(100001)]
visited[n] = 0

# 목적지까지 최단 거리(시간)를 구하는 문제이기 때문에 BFS
def bfs(v):
    q = deque()
    q.append(v)
    while q:
        now = q.popleft()
        # 만약 그 수가 바로 맞으면 바로 출력하기
        if now == k:
            return visited[now]
            
        for i in (now + 1, now - 1, now * 2):
            if 0 <= i <= 100000 and visited[i] == -1:
                if i == now * 2:
                    visited[i] = visited[now]
                    q.appendleft(i)
                else:
                    visited[i] = visited[now] + 1
                    q.append(i)

answer = bfs(n)
print(answer)
