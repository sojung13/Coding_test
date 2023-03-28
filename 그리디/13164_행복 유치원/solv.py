import sys
sys.stdin = open('input.txt','r')

n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr2 = []

for i in range(n-1):
    gap = arr[i+1] - arr[i]
    arr2.append(gap)

arr2.sort()
cost = 0

for i in range(n-k):
    cost += arr2[i]

print(cost)