import sys
sys.stdin = open('input.txt','r')

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())
    answer = 0
    for row in range(i-1,x):
        for col in range(j-1,y):
            answer += arr[row][col]
    print(answer)
