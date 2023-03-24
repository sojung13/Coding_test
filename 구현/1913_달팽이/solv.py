import sys
sys.stdin = open('input.txt','r')

n = int(input())
num = int(input())
snail = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

i = 2
start = 3

for i in range(n):
    