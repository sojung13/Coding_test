import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))


for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    answer = 0
    for row in range(x1-1,x2):
        for col in range(y1-1,y2):
            answer += arr[row][col]
    print(answer)