import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    cnt = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == '*':
                    continue
                elif arr[nx][ny]
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input().split()))
print(arr)