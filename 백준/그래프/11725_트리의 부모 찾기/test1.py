# 런타임 에러 (RecursionError)
import sys
sys.stdin = open("input.txt", "r")
from collections import deque
def dfs(start):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            dfs(i)

N = int(input())
graph = [[] for _ in range(N+1)]
input = sys.stdin.readline

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()

# dfs
visited = [0] * (N+1)
dfs(1)

for _ in range(2, N+1):
    print(visited[_])