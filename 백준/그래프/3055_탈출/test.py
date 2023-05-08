import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고
            if 0 <= nx < r and 0 <= ny < c:
                # 만약 D 도착하면 출력하기
                if arr[nx][ny] == 'D':
                    visited[nx][ny] = visited[x][y] + 1
                    print(visited[nx][ny])
                    return
                # 만약 현재 길이고 다음도 길이면
                elif arr[nx][ny] == '.' and visited[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
        water()
    print("KAKTUS")
    return

def water():
    x,y = wq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
            arr[nx][ny] = '*'
            wq.append((nx,ny))


r,c = map(int,input().split())
arr = [list(map(str, input())) for _ in range(r)]
visited = [[0]*c for _ in range(r)]
wq = deque()
x,y = 0,0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            x,y = i,j
        elif arr[i][j] == '*':
            wq.append((i,j))
water()
bfs(x,y)