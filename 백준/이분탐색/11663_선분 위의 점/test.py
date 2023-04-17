import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(m):
    start , end = map(int,input().split())
    cnt = 0
    for i in arr: # 1 3 10 20 30
        for j in range(start, end + 1):
            if i == j:
                cnt += 1
    print(cnt)