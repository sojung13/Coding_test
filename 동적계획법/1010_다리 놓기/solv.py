import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]

