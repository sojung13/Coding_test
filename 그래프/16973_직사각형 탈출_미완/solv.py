import sys
sys.stdin = open('input.txt','r')

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# def bfs


n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
h,w,ss,sc,fr,fc = map(int,input().split())
