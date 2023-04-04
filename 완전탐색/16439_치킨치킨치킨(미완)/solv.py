import sys
sys.stdin = open('input.txt','r')
from itertools import combinations

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

maxSum = 0
for a,b,c in combinations(range(m),3):
    print(a,b,c)
    tmpSum = 0
    for i in range(n):
        tmpSum += max(arr[i][a], arr[i][b], arr[i][c])
    maxSum = max(maxSum, tmpSum)
print(maxSum)