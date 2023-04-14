import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

n,m = map(int,input().split())
wait = [int(input()) for _ in range(n)]
start, end = min(wait), max(wait)*m
while start <= end:
    mid = (start + end) // 2
    time = 0
    for i in range(n):
        time += mid // wait[i]
    if time >= m:
        end = mid - 1
    else:
        start = mid + 1
print(end+1)