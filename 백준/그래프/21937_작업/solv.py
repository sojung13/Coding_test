import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    for i in arr[x]: # 일단 5 선과목 1,4가 들어온다
        if visited[i] == False:
            dfs(i)
            cnt += 1
cnt = 0
n,m = map(int,input().split())
arr = [[]*(m+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[b].append(a)
x = int(input())
visited = [False] * (n+1)
dfs(x)
print(cnt)
