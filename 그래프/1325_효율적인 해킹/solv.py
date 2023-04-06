import sys
sys.stdin = open('input.txt','r')
from collections import deque

n,m = map(int,input().split())
arr = [[False]*(n+1) for _ in range(m+1)]
for _ in range(m):
    i,j = map(int,input().split())
    arr[j][i] = True
visited = [False for _ in range(n+1)]

def bfs():
    q = deque()
    q.append()
    while q:
